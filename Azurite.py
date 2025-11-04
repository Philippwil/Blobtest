from azure.storage.blob import BlobServiceClient
import os

# Lokale Verbindung zu Azurite
connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

# BlobServiceClient erstellen
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

start=True
while start==True:
    hallo=print("Hallo!\nBitte nennen sie zuerst den Namen ihres Containers auf, den Sie nutzen wollen. Wenn Sie einen neuen Container erstellen wollen, dann schreiben Sie diesen Namen auf:")
   
    # Container-Name (muss existieren oder wird erstellt)
    container_name =input(">>>")
    container_client = blob_service_client.get_container_client(container_name)

    # Container anlegen (falls noch nicht vorhanden)
    try:
        container_client.create_container()
        print(f"Container '{container_name}' erstellt.")
    except Exception as e:
        print(f"Container existiert vermutlich schon oder anderer Fehler: {e}")
    containers = [c.name for c in blob_service_client.list_containers()]
    print("Aktuelle Container:", containers)
    menu=0
    while menu !=3:
        print("Blobs im Container:")
        for blob in container_client.list_blobs():
            print(" -", blob.name)
        print("\n")
        menu=int(input("Was möchten Sie machen?\n|1|Datei erstellen\n|2|Datei Herunterladen\n|3|Zurück\n|4|Schließen\n>>>"))
        if menu == 1:
        
            # Lokale Datei erstellen
            local_file_name =input("Name der Datei(Mit dateiformat)\n>>>")
            blob_client = container_client.get_blob_client(local_file_name)
            local_file_path = os.path.join(".", local_file_name)

            with open(local_file_path, "w", encoding="utf-8") as file:
                inhalt=input("Schreiben Sie den inhalt der Datei\n>>>")
                file.write(inhalt)

            # Datei hochladen
            blob_client = container_client.get_blob_client(local_file_name)
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

            print(f"Datei '{local_file_name}' erfolgreich hochgeladen!")
            menu =0
        elif menu == 2:
            # Datei wieder herunterladen
            local_file_name =input("Name der Datei(Mit dateiformat)\n>>>")
            blob_client = container_client.get_blob_client(local_file_name)
            download_file_path = os.path.join(".Download\\" + local_file_name)
            with open(download_file_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())

            print(f"⬇️  Datei heruntergeladen als '{download_file_path}'")
            menu=0
        elif menu == 4:
            start =False
            break
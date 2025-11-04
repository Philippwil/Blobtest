1.  Microsoft Azure Storage Explorer über den link [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/?msockid=1fc582e0b11e6e2e05179472b0466fb1)
    herunterladen
2.  Docker muss laufen
3.  Im Command Prompt folgende Code nacheinander ausführen:
    -   docker run -d -p 10000:10000 -p 10001:10001 -p 10002:10002 -v azurite_data:/data --name azurite mcr.microsoft.com/azure-storage/azurite
    -   pip install azure-storage-blob
5.  Ordner mit dem Namen "Download" erstellen
6. Python Datei "Azurite.py" ausführen
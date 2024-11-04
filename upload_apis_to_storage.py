""""upload api to storage vector database"""

import keyring

from azure.storage.blob import BlobServiceClient
import os

def upload_files_to_blob_storage(container_name, connection_string, folder_path):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            blob_client = container_client.get_blob_client(file)
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
                print(f"Uploaded {file_path} to {container_name}")

# Usage
storage_connection_string = keyring.get_password("storage-connection-string", "xxx")
container_name = "api-container"
folder_path = "generated_api"
upload_files_to_blob_storage(container_name, storage_connection_string, folder_path)
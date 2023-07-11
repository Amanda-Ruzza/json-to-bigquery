import sys
import logging
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    logging.info(f"File {source_file_name} uploaded to {destination_blob_name}.")




if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    upload_blob(
        bucket_name=sys.argv[1],
        source_file_name=sys.argv[2],
        destination_blob_name=sys.argv[3],
    )
    
import sys
import logging
import json
from google.cloud import storage


def process_json_file(json_file_path, output_file_path):
    """Parses the raw JSON file and creates a new line-delimited JSON file for BigQuery."""
    with open(json_file_path) as json_file:
        raw_data = json.load(json_file)

    events = raw_data.get("recommendations", [])

    with open(output_file_path, 'w') as output_file:
        for event_data in events:
            event = event_data.get("event", {})
            output_file.write(json.dumps(event) + '\n')

    logging.info(f"New line-delimited JSON file created: {output_file_path}")
    

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    logging.info(f"File {source_file_name} uploaded to {destination_blob_name}.")




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # JSON file paths
    json_file_path = "nyc_band_events2.json"
    ndjson_file_path = "nyc_band_events2.ndjson"  # Output file path for new line-delimited JSON
    
    # Process JSON file and create new line-delimited JSON
    process_json_file(json_file_path, ndjson_file_path)
    
    # Upload new line-delimited JSON file to GCP bucket
    upload_blob(
        bucket_name=sys.argv[1],
        source_file_name=ndjson_file_path,
        destination_blob_name=sys.argv[2],
    )
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "cr-lab-aruzza-2706230354.seatgeeks.events_nyc"

job_config = bigquery.LoadJobConfig(
    # figure out the auto-schema
    # schema=[
    #     bigquery.SchemaField("name", "STRING"),
    #     bigquery.SchemaField("post_abbr", "STRING"),
    # ],
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)
uri = "gs://cloud-samples-data/bigquery/us-states/us-states.json"

load_job = client.load_table_from_uri(
    uri,
    table_id,
    location="US",  # Must match the destination dataset location.
    job_config=job_config,
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))
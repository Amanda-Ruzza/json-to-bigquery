# README #

This project contains two Python scripts that:
    * Transforms a raw JSON file extracted from the 'SeatGeek API' into a ``ndjson`` format for BigQuery usage
    * Loads the file into BigQuery


### How do I get set up? ###

* Dependencies
The necessary packages are listed in ``requirements.txt``
The raw file needs to be located in the same local directory of this project

* Deployment instructions
1 - Authenticate with the target GCP account.
2 - Run the transformation script by inputting these values on the terminal:
```
python bucket_obj_upload.py <bucket-name> <raw-file.json> <transformed-file.ndjson>
```
Example:
```
python bucket_obj_upload.py cr-lab-aruzza-ae7140b2-seatgeeks nyc_band_events2.ndjson
```
3 - Run ``python bq_load.py`` to upload the transformed data into BigQuery

### Future Improvements ###

* Use the ``sys`` module to remove hard-coded values and create CLI arguments to be passed when the scripts are run

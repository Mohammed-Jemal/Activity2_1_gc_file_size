import sys
from google.cloud import storage
import os

def download_file(bucket_name, blob_name):
    try:
        # Initialize a client
        client = storage.Client()

        # Get the bucket
        bucket = client.get_bucket(bucket_name)

        # Get the blob (file) from the bucket
        blob = bucket.get_blob(blob_name)

        if blob is None:
            raise Exception("Blob not found.")

        # Get the size of the blob in bytes
        size_in_bytes = blob.size
 	print(f"The size of the file is: {size_in_bytes} bytes")
    except Exception as e:
        print("Error downloading file from GCP Storage:", e)
if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Incorrect number of command-line arguments")
        print("Usage: python3 activ2_1.py <bucket_name> <blob_name>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    blob_name = sys.argv[2]

    download_file(bucket_name, blob_name)
from google.cloud import storage
import os

# Set via environment or replace directly
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

def upload_file(bucket_name, source_file, destination_blob):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"[✓] Uploaded {source_file} to {bucket_name}/{destination_blob}")

# Example usage
upload_file("my-bucket-name", "localfile.txt", "cloudfolder/localfile.txt")

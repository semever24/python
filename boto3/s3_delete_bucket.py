import boto3
from botocore.exceptions import ClientError

def delete_bucket(bucket_name, region="ap-south-1"):
    s3 = boto3.client("s3", region_name=region)
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully")
    except ClientError as e:
        print(f"Error deleting bucket: {e}")

delete_bucket("boto3-demo-bucket-sk-001")
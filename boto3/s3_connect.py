import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

def create_bucket(bucket_name, region='ap-south-1'):
    try:
        s3_client = boto3.client('s3', region_name=region)
        
        # for "us-east-1" no LocationConstraint block required
        # s3_client.create_bucket(Bucket=bucket_name)

        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )

    except ClientError as e:
        logging.error(f"Bucket creation failed: {e}")
        return False

    logging.info(f"Bucket '{bucket_name}' created successfully")
    return True


create_bucket("boto3-demo-bucket-sk-001", "ap-south-1")
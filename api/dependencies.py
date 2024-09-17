import config
from functools import lru_cache
from dotenv import load_dotenv
from fastapi import HTTPException,status
import boto3
import os

load_dotenv(override=True)
@lru_cache
def get_settings():
    return config.Settings()

AWS_bucket = get_settings().AWS_BUCKET

s3_low_level = boto3.client("s3")
location = s3_low_level.get_bucket_location(Bucket=AWS_bucket)

# High level wrapper
s3 = boto3.resource(service_name="s3")

bucket = s3.Bucket(name=AWS_bucket)
# Handle the case where LocationConstraint is None (which indicates 'us-east-1')
region = location['LocationConstraint'] or 'us-east-1'

def aws_upload_file(file_obj,filename:str) -> str:
    try:
        bucket.upload_fileobj(file_obj, filename)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong uploading to AWS")
    link = f"https://{AWS_bucket}.s3.{region}.amazonaws.com/{filename}"
    return link
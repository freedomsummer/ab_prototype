import boto3
import os
s3 = boto3.client(
    's3',                   
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),                   
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),                   
    region_name='us-west-2'
)
print(s3)
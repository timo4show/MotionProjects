import os
import boto3

s3 = boto3.resource('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    bucket_name = os.environ.get('bucket_name')
    bucket = s3.Bucket(bucket_name)

    for obj in bucket.objects.all():
        obj.delete()

    if len(list(bucket.objects.all())) > 0:
        message = 'There are

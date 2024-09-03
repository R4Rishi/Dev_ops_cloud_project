import boto3
import os
import json
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = os.environ['SOURCE_BUCKET']
    backup_bucket = os.environ['BACKUP_BUCKET']
    
    # we need to get the current date to create a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # objects in the source bucket
    response = s3.list_objects_v2(Bucket=source_bucket)

    if 'Contents' not in response:
        print("No files found in the source bucket.")
        return

    for obj in response['Contents']:
        #  we need to Create a new object key for the backup with a timestamp
        backup_key = f"{timestamp}/{obj['Key']}"
        
        # Copy the created object to backup bucket
        copy_source = {'Bucket': source_bucket, 'Key': obj['Key']}
        s3.copy_object(CopySource=copy_source, Bucket=backup_bucket, Key=backup_key)
        print(f"Backup created for {obj['Key']} as {backup_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Backup completed successfully!')
    }

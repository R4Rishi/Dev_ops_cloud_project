import boto3
import os
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    backup_bucket = os.environ['BACKUP_BUCKET']
    restore_bucket = os.environ['RESTORE_BUCKET']
    
    # Get the list of objects in the backup bucket
    response = s3.list_objects_v2(Bucket=backup_bucket)

    if 'Contents' not in response:
        print("No backup files found.")
        return

    for obj in response['Contents']:
        # let's Copy object back to the original bucket
        restore_key = obj['Key'].split('/', 1)[-1]  # if needed Remove the timestamp from the key
        copy_source = {'Bucket': backup_bucket, 'Key': obj['Key']}
        s3.copy_object(CopySource=copy_source, Bucket=restore_bucket, Key=restore_key)
        print(f"Restored {obj['Key']} to {restore_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Restore completed successfully!')
    }

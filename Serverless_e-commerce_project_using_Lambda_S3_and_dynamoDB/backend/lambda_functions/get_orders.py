# lambda_functions/get_orders.py

import boto3
import json
import os

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Scan the DynamoDB table to get all orders
        response = table.scan()
        orders = response.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(orders)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error retrieving orders', 'error': str(e)})
        }

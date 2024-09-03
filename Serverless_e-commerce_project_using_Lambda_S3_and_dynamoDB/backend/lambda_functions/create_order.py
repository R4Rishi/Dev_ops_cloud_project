# lambda_functions/create_order.py

import boto3
import json
import os
from uuid import uuid4

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        order = json.loads(event['body'])
        
        # Validate order structure
        if not all(key in order for key in ('customer', 'products')):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid order structure'})
            }

        # Generate a unique order ID
        order['id'] = str(uuid4())

        # Insert the order into DynamoDB
        table.put_item(Item=order)

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Order created successfully', 'orderId': order['id']})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error creating order', 'error': str(e)})
        }

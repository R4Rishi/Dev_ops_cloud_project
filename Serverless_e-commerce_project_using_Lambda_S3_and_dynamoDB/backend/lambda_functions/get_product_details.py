# lambda_functions/get_product_details.py

import boto3
import json
import os

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    product_id = event.get('pathParameters', {}).get('productId')
    
    if not product_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Product ID is required'})
        }
    
    try:
        # Get the product details from S3
        response = s3.get_object(Bucket=os.environ['S3_BUCKET_NAME'], Key='product-details.json')
        product_data = json.loads(response['Body'].read())

        # Find the product by ID
        product = next((item for item in product_data if item['id'] == product_id), None)

        if not product:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Product not found'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps(product)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error retrieving product details', 'error': str(e)})
        }

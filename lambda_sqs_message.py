import boto3 
import json
from datetime import datetime

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    sqs.send_message(
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/061354871783/Project',
        MessageBody = current)
    return {
        'statusCode': '200',
        'body': json.dumps(current)
    }

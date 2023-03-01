import boto3 
import json
from datetime import datetime

def lambda_handler(event, context):
    sqs = boto3.client('sqs')  # creating sqs client
    now = datetime.now() # using the now() function to get a datetime object containing current date and time.
    current = now.strftime("%H:%M:%S") # using datetime.strftime() function to create a string representing 
     # the current time
     
    sqs.send_message(  # sending the message to the sqs queue
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/061354871783/Project', # sqs queue url
        MessageBody = current)
    return {
        'statusCode': '200',
        'body': json.dumps(current)
    }

import boto3  #importing boto3 module 

sqs = boto3.client('sqs', region_name = 'us-east-1')  #creating an sqs low-level client

response = sqs.create_queue(
    QueueName='Project')  #name of queue
print(response)
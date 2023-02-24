import boto3  #importing boto3 module

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Flowers')

response = table.delete()

print(response)
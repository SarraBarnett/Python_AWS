import boto3 # importing boto3 module

# to add conditions to scanning and querying a table,
# you need to import this module:
from boto3.dynamodb.conditions import Key 

dynamodb = boto3.resource('dynamodb') # getting the AWS Dynamodb serivce resource

table = dynamodb.Table('Flowers') # assigning "table" variable as my Flowers table

# querying for the flower key that equals Rose
response = table.query(
    KeyConditionExpression=Key('Flower').eq('Rose')
)
items = response['Items']
print(items)
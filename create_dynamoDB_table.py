# Create a DynamoDB Table:

import boto3   # importing the boto3 module

dynamoDB = boto3.resource('dynamodb')   # creating a resource to AWS Dynamodb serivce

response = dynamoDB.create_table(   # create_table operation adds a new table to  
    # your account
    
    TableName = 'Flowers',
    
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,  # number of reads per second
        'WriteCapacityUnits': 10  # number of writes per second
    },
    
     KeySchema = [   # attributes that make up the composite primary key
        {
            'AttributeName': 'Flower',
            'KeyType': 'HASH' # partition key
        },
        {
            'AttributeName': 'Family',
            'KeyType': 'RANGE' # sort key
        },
    ],
    
    AttributeDefinitions = [  # data types for the key schema attributes
        {
            'AttributeName': 'Flower',
            'AttributeType': 'S'  # string
        },
        {
            'AttributeName': 'Family',
            'AttributeType': 'S'  # string
        },
    ],

)

print(response)
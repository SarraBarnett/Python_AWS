import boto3  # importing boto3 module

dynamodb = boto3.resource('dynamodb')  # getting dynamodb service resource

table = dynamodb.Table('Flowers')  # assigning table variable

# deleting an item
response = table.delete_item(
    Key = {'Flower':'Daisy', 'Family':'Asteraceae'})
    
print(response)
# Add multiple items to a dynamoDB Table:

import boto3   # importing boto3 module

dynamoDB = boto3.resource('dynamodb')   # getting the AWS Dynamodb serivce resource

table = dynamoDB.Table('Flowers')   # assigning "table" variable as my Flowers table

with table.batch_writer() as batch:   # putting multiple items in the table at once
    batch.put_item(Item = {"Flower": "Rose", "Family": "Rosaceae"}),
    batch.put_item(Item = {"Flower": "Petunia", "Family": "Solanaceae"}),
    batch.put_item(Item = {"Flower": "Lily", "Family": "Liliaceae"}),
    batch.put_item(Item = {"Flower": "Daisy", "Family": "Asteraceae"}),
    batch.put_item(Item = {"Flower": "Carnation", "Family": "Caryophyllaceae"}),
    batch.put_item(Item = {"Flower": "Gardenia", "Family": "Rubiaceae"}),
    batch.put_item(Item = {"Flower": "Peony", "Family": "Paeoniaceae"}),
    batch.put_item(Item = {"Flower": "Orchid", "Family": "Orchidaceae"}),
    batch.put_item(Item = {"Flower": "Daffodil", "Family": "Amaryllidaceae"}),
    batch.put_item(Item = {"Flower": "Tulip", "Family": "Liliaceae"})
    
print(table)
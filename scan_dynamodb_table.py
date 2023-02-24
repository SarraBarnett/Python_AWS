import boto3   # importing boto3 module

dynamodb = boto3.resource('dynamodb')  # getting the Dynamodb serivce resource

table = dynamodb.Table("Flowers")  # assigning "table" variable as my Flowers table

response = table.scan()  # assigning the scan function

# using a for loop to print out items in a list
for item in response["Items"]:
    print(item)
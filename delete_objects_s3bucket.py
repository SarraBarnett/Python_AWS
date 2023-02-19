#!/usr/bin/env python3.7

import boto3

### how to delete a single object

s3_resource = boto3.client("s3")

s3_resource.delete_object(Bucket = "week14mondayluit2", Key = "pets.jpg")



### how to delete multiple objects

# find all the objects from the bucket
objects = s3_resource.list_objects(Bucket = "week14mondayluit2")["Contents"]

# print how many objects are in the bucket 
print(len(objects))

# iteration deletion of objects
for object in objects:
    response = s3_resource.delete_object(Bucket = "week14mondayluit2", Key = object["Key"])
    print(response)   #print response of deleted object
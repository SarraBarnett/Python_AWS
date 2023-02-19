#!/usr/bin/env python3.7

import boto3
import os
import glob 

# how to upload a single file to s3 bucket 

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename = "jack.jpg",
    Bucket = "week14mondayluit2",
    Key = "jacktest.jpg")
    
# how to upload multiple files

cwd = os.getcwd()
cwd = cwd + "/Python_AWS/"
files = glob.glob(cwd + "*.jpg")

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename = file,
    Bucket = "week14mondayluit2",
    Key = file.split("/")[-1])
    

### how to list objects in multiple ways

s3_resource = boto3.client("s3")

objects = s3_resource.list_objects(Bucket = "week14mondayluit2")["Contents"]

# prints how many objects are in the bucket
print(len(objects))

# prints string if there are 1 or more objects in the bucket
if len(objects)>0:
    print("objects exists")

# prints objects in a column   
for object in objects:
    print(object)


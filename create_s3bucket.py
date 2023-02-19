#!/usr/bin/env python3.7

import boto3

# setting aws_resource as the value of s3
aws_resource = boto3.resource("s3")

# naming a bucket 
bucket = aws_resource.Bucket("week14mondayluit2")

# creating a bucket 
response = bucket.create(
    ACL= 'private',  
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)
print(response)
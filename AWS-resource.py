#!/usr/bin/env python3.7

import boto3

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("LUIT-Redweek14")

response = bucket.create(
    ACL= 'public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
)
print(response)
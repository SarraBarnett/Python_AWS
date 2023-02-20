#!/usr/bin/env python 3.7

### How to get all ec2 instance Id's

import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for each in response['Reservations']:
    for instance in each['Instances']:
        print(instance['InstanceId'])
    



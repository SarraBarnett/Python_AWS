#!/usr/bin/env python3.7


# How to remove your AWS vpc

# Can't delete vpc if there are other resources and gateways attached:
# like ec2 instances, route tables(except default), and
# security groups(except default)


import boto3

client = boto3.client("ec2")

response = client.delete_vpc(
    VpcId = 'vpc-098b28ba93af7f4c4'
    )
print(response)
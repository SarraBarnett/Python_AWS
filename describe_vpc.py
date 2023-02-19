#!/usr/bin/env python3.7

import boto3

client = boto3.client("ec2")

### How to describe all vpc's available in your account

x = client.describe_vpcs()

num_of_vpcs = x["Vpcs"]

print(len(num_of_vpcs))

# print out vpc ID of each vpc
for vpc in num_of_vpcs:
    print(vpc["VpcId"])
    
### How to describe one vpc based on vpc ID

x = client.describe_vpcs(VpcIds=["vpc-098b28ba93af7f4c4"])
#!/usr/bin/env python3.7

### terminate multiple ec2 instances

import boto3

ec2_client = boto3.client("ec2")

x = ec2_client.describe_instances()

data = x["Reservations"]

# make an empty list
li = []

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id = ids["InstanceId"]
        li.append(instance_id)  # appending instance ids to "li" list 
        

# terminate all instance ids in the list
ec2_client.terminate_instances(InstanceIds=li)
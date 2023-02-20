#!/usr/bin/env python3.7

# How to describe ebs volume snapshot

import boto3

ec2_client = boto3.client("ec2")

print(ec2_client.describe_snapshots(SnapshotIds=[
    'snap-0891d28e9cca1e9e5']))
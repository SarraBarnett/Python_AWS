#!/usr/bin/env python3.7

# How to delete an ebs volume snapshot

import boto3

ec2_client = boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId = 'snap-022ad3dfc931ef4ad')
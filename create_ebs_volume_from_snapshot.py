#!/usr/bin/env python3.7

# How to create an ebs volume from a snapshot 

import boto3

ec2_client = boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone = 'us-east-1b',
    Encrypted = True,
    Size = 12,
    SnapshotId = 'snap-022ad3dfc931ef4ad',
    VolumeType = 'gp2')

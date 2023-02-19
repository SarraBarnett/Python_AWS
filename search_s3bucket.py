#!/usr/bin/env python3.7

import boto3

# assign resource variable with value of s3

resource = boto3.resource("s3")

### to print out each bucket:


# use a for loop to print out each bucket

for bucket in resource.buckets.all():
    print(bucket.name)
    
    
    
### to search for how many buckets you have:  



# assign all buckets to a list, "bucket_list"

bucket_list = list(resource.buckets.all())

# print out length of the bucket_list which specifies how many there are

print("Number of Buckets =", (len(bucket_list)))



### print creation date for each bucket:



# create a low-level s3 service client 

s3_resource = boto3.client("s3")

s3_resource.list_buckets()["Buckets"][0]["Name"]

creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

creation_date.strftime("%d%m%y_%H:%M:%s")

# use a for loop to print out each bucket with its name and creation date/time

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
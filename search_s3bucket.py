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
import time

import boto3
import csv
import json
# with open('/Users/ankur/Desktop/emp.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['First Name'], row['Last Name'])
my_stream_name = 'stream1'
thing_id ='XYZ'
kinesis_client = boto3.client('kinesis', region_name='ap-south-1')

with open('/Users/ankur/Desktop/emp4.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        put_response = kinesis_client.put_record(
                StreamName=my_stream_name,
                Data=json.dumps(row),
                PartitionKey=thing_id)
        print(put_response)
        time.sleep(5)
print("hello")

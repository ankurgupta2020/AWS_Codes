import json
import os
import boto3
import csv
s3 = boto3.client('s3')
def lambda_handler(event,  context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        csvfile = s3.get_object(Bucket=bucket, Key=file_key)
        csvcontent = csvfile['Body'].read().decode('utf-8').splitlines()
        print(csvcontent)
        lines = csv.reader(csvcontent)
        headers = next(lines)
        print('headers: %s' %(headers))
        for line in lines:
            read_ind=line[2]
            if read_ind=='Y':
                print("File_Name: ",line[0]," || ", "File_Path : ",line[1])
                obj=s3.get_object(Bucket=bucket, Key=line[1])
                content = obj['Body'].read().decode('utf-8')
                print(content)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

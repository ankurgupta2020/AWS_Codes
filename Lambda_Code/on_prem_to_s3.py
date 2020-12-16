import boto3

# Create S3 resource
s3 = boto3.resource('s3')
# Initalize variables
bucket_name = 'himym'
on_prem_path = '/Users/ankur/Desktop/emp4.csv'
key= "emp4.csv"
# Put Object
s3.Bucket(bucket_name).upload_file(on_prem_path
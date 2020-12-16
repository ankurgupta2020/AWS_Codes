# S3 COPY BUCKET
# ---------------

# Original Code
import json
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")


def lambda_handler(event, context):
   destination_bucket_name = 'demobucketag-2'

   # event contains all information about uploaded object
   print("Event :", event)

   # Bucket Name where file was uploaded
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path)
   file_key_name = event['Records'][0]['s3']['object']['key']

   # Copy Source Object
   copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

   # S3 copy object operation
   s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)

   return {
       'statusCode': 200,
       'body': json.dumps('Hello from S3 events Lambda!')
   }


# Modified Code
import json
import boto3

s3_client = boto3.client("s3")


def lambda_handler(event, context):
   destination_bucket_name = 'demobucketag-3'
   print("Event :", event)
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']
   file_key_name = event['Records'][0]['s3']['object']['key']
   copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}
  
   list1=file_key_name.split('/')
   name=list1[-1]
  
   dest_file_key_name= 'p2/' + name
   s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=dest_file_key_name)
   return {
       'statusCode': 200,
       'body': json.dumps('Hello from S3 events Lambda!')
   }







import json
import boto3
import base64

def lambda_handler(event, context):
    # TODO implement
    s3_client = boto3.client('s3')
    bucket_name = "kinesis-to-s3bucket"
    s3_file_name = 'emp.csv'
    resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    data1 = resp['Body'].read().decode('utf-8')
    print(data1)
    for record in event["Records"]:
        decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print(decoded_data)
        
        res = json.loads(decoded_data) 
        print(res)
        data = data1 + "\n"+res["Emp_id"]+","+res["Emp_Name"]+","+res["Location"]+","+res["Salary"]
        print (data)
        s3client = boto3.client('s3')
        s3client.put_object(Body=data,Bucket="kinesis-to-s3bucket", Key='emp.csv')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

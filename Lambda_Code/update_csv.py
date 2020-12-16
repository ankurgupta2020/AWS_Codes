import json
import os
import boto3
import csv
import codecs
from io import StringIO
s3 = boto3.client('s3')
def lambda_handler(event,  context):
        # create s3 resource and config bicket name and object
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('prob-2-config')
        obj = bucket.Object(key = 'emp2.csv')
        stream = codecs.getreader('utf-8')(obj.get()['Body'])
        # DictReader maps the information read into a dictionary
        lines = list(csv.DictReader(stream))
        # StringIO create object file which can be treated as file
        csv_buffer = StringIO()
        #Maps Python dictionaries into CSV rows
        out = csv.DictWriter(csv_buffer, fieldnames=['emp_id','first_name','dept_name','salary'])
        for row in lines:
            if row['dept_name'] == "": #first second and last dept name

                out.writerow({'emp_id':row['emp_id'],'first_name':row['first_name'],'dept_name': 'Research','salary':row['salary']})
                continue
            if row['salary'] =="153790.0": #Fourth Salary
                # sal=str(sal)
                sal=float(row['salary'])+2000.0
                sal=str(sal)
                print("In sal\n",sal)
                out.writerow({'emp_id':row['emp_id'],'first_name':row['first_name'],'dept_name':row['dept_name'],'salary':sal})
                continue
            out.writerow({'emp_id':row['emp_id'],'first_name':row['first_name'],'dept_name':row['dept_name'],'salary':row['salary']})
        # Put csv back in CSV    
        s3client = boto3.client('s3')
        s3client.put_object(Body=csv_buffer.getvalue().encode("utf8"),Bucket='prob-2-config', Key='new_employee.csv')
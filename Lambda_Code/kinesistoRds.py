import boto3
import pymysql
import base64
import sys
import logging
import pymysql
import json
#rds settings
rds_host  = "emp.cfjk3brvx09i.us-east-2.rds.amazonaws.com"
name = "admin"
password = "lab-password"
db_name = "emp"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    for record in event["Records"]:
        decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        res = json.loads(decoded_data) 
        print(res)
    
    with conn.cursor() as cur:
    
        insert_stmt = (
        "INSERT INTO Empt1 (EmpID, Name, First_Name, Middle_Initial, Last_Name, Gender, EMail, FatherName, MotherName, DoB, Age, Weight, DoJ, Salary, SSN, Ph, County, City, State, Zip, Region, User_Name, Pass) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
        )
        # add_employee = ("INSERT INTO test2 "
        #                 "(Emp_ID, last_name, hire_date, gender, birth_date) "
        #                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)")
        # data=(123456,"Ankur","Gupta")
       
        data = (res['Emp ID'],res['Name Prefix'],res['First Name'],res['Middle Initial'],res['Last Name'],res['Gender'],res['E Mail'],res["Father's Name"],res["Mother's Name"],res['Date of Birth'],res['Age in Yrs.'],res['Weight in Kgs.'],res['Date of Joining'],res['Salary'],res['SSN'],res[ 'Phone No. '],res['County'],res['City'],res['State'],res['Zip'],res['Region'],res['User Name'],res['Password'])
        
        cur.execute(insert_stmt, data)          
        # cur.execute('insert into test1 (Name) values("'+str(emp[1])+'")')
        conn.commit()
        
        
      
    
        

    return True

    



# def lambda_handler(event, context):
#     # rds_endpoint  = "emp.cfjk3brvx09i.us-east-2.rds.amazonaws.com"
#     # username = "admin"
#     # password = "lab-password" # RDS Mysql password
#     # db_name = "emp" # RDS MySQL DB name
#     # conn = None
#     # try:
#     #     conn = pymysql.connect(rds_endpoint, user=username, passwd=password, db=db_name, connect_timeout=5)
#     #     print("Success")
#     # except pymysql.MySQLError as e:
#     #     print("ERROR: Unexpected error: Could not connect to MySQL instance.")
#     for record in event["Records"]:
#         decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
#         print(decoded_data)
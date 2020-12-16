#Lambda 1
import json

def lambda_handler(event, context):
    
    input_param = {
        "carName" : "Honda",
        "condition" : "good",
        "howold" : "5"    
    }
    
    print("responceFromChildLambda ",input_param)
    return input_param



# Lambda 2
import json

def lambda_handler(event, context):
  
    
        carName = event['carName']
        condition = event['condition']
        howold = event['howold']
        
        price = getCarPrice(carName, condition, howold)
        print("Carprice : ",price)
        
        return {
            'carName' : carName,
            'condition' :  condition,
            "howold" : howold,
            'price' : price
        }
    
def getCarPrice(carName, condition, howold):
    print(carName, " ", condition, " ", howold)
        
    if (carName == "Honda" and condition == "good" and int(howold) <= 5):
            return "7 Lakh"
    elif(carName == "Honda" and condition == "good" and int(howold) > 5):
            return "5 Lakh"
    else:
            return "2 Lakh"

# Step function
 {
  "Comment": "A Hello World example of the Amazon States Language using Pass states",
  "StartAt": "First",
  "States": {
    "First": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-west-2:464088672461:function:first",
      "Next": "Second"
    },
    "Second": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-west-2:464088672461:function:second",
      "End": true
    }
  }
}
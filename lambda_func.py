import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('esa_db_test')

def lambda_handler(event, context):
    response = table.put_item(
        Item={
              'aalias': event['aalias'],
              "simid":event['simid'],
    		  "q1":event['q1'],
    		  "q2":str(event['q2']),
    		  "q3":event['q3'],
    		  "q4":event['q4'],
    		  "q5":event['q5'],
    		  "q6":event['q6'],
    		  "q7":event['q7'],
    		  "q8":event['q8'],
    		  "q9":event['q9'],
    		  "q10":event['q10'],
    		  "q11":event['q11'],
    		  "q12":event['q12'],
    		  "q13":event['q13'],
    		  "q14":event['q14']
            })
    return {
        'statusCode': 200,
        'body': json.dumps('form submitted by:' + event['aalias'])
    }
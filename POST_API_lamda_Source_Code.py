import boto3

def lambda_handler(event, context):
   client_config = boto3.resource('dynamodb')
   table = client_config.Table('Accounts')
   response = table.put_item(
       Item={

           'id': event['id'],
           'title': event['title'],
           'description': event['description'],
           'date': event['date']

       }
   )

   return {
       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
       'body': 'Record ' + event['id'] + ' added'
   }
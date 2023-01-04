import boto3

def lambda_handler(event, context):
   client_config = boto3.resource('dynamodb')
   table = client_config.Table('Accounts')
   response = table.get_item(
       Key={
           'id': event['id']
       }
   )

   if 'Item' in response:
       return response['Item']
   else:
       return {
           'statusCode': '404',
           'body': 'Announcement not available'
       }
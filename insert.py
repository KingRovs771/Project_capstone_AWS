import boto3
table = boto3.client('dynamodb', region_name='us-east-1')

response = table.put_item( 
    TableName='user', 
        Item={
             "userId": {"S": "12"},
             "email": {"S": "email@example.com"},
             "username": {"S": "username"},
             "password": {"S": "password"}
        } 
) 
print("Item baru telah ditulis:", response)
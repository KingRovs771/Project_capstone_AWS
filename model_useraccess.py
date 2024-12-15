import boto3

dynamodhb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodhb.create_table(
    TableName='user_access',
    KeySchema =[
        {
            'AttrubuteName' : 'username',
            'KeyType' : 'HASH'
        }
    ],
    AttributeDefinitions =[
        {
            'AttributeName' : 'username',
            'AttributeType' : 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits' : 5,
        'WriteCapacityUnits' : 5,
    }
)


table.meta.client.get_waiter('table_exists').wait(TableName='user_access')
print('Table User Access Telah Dibuat')
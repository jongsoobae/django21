import boto3
from boto3.dynamodb.conditions import Key, Attr, Contains


def contains(self, value):
    return Contains(self, value)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('js_files')


response = table.query(
    KeyConditionExpression=Key('folder').eq('stock'),
    FilterExpression=Attr('filename').contains('bb')
)

print(response)

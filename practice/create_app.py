import boto3

client = boto3.client('pinpoint')
response = client.create_app(
    CreateApplicationRequest={
        'Name': 'Test',
        'tags': {
            'string': 'Python-test'
        }
    }
)
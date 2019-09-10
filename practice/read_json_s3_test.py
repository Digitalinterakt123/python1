import boto3
import json

# # data = {"HelloWorld": []}
# s3 = boto3.resource('s3')
# obj = s3.Object('diawspinpoint','ji2019/08/09/04/hello-1-2019-08-09-04-34-58-2c80cdfe-eb8c-4cd9-9846-1971e9ca6924')
# data = obj.get()['Body'].read().decode('utf-8')
# # print(data[209:236],' , ',data[848:869])
# for info in data:
#     print(data['event_type'])

dynamodb=boto3.resource('dynamodb')
bucket_name= 'diawspinpoint'
key1 = 'ji2019/08/09/04/hello-1-2019-08-09-04-40-02-e0d11cd7-b626-4646-bce4-537ce4c9e22f'
s3 = boto3.client('s3', aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY')
obj = s3.get_object(Bucket=bucket_name, Key=key1)
data = (line.decode('utf-8') for line in obj['Body'].iter_lines())
i = 1
for row in data:
    data1 = json.loads(row)
    Event = str(data1['event_type'])
    Client_id = str(data1['client']['client_id'])
    Receipient = str(data1['facets']['email_channel']['mail_event']['mail']['destination'][0])
    item = {'SNO' : i, 'Event' : Event,'Client_id' : Client_id, 'Receipient' : Receipient}
    table = dynamodb.Table('Openers1')
    table.put_item(Item=item)
    print(item)

    # print('SNO : ',i,',','Client_id : ',Client_id ,',', 'Receipient : ',Receipient )
    # print('Receipient : ', str(data1['facets']['email_channel']['mail_event']['mail']['destination'][0]))
    i = i +1

import boto3
import json
from datetime import datetime
from dateutil.parser import parse


s3 = boto3.resource('s3')

my_bucket = s3.Bucket('di-aws-pinpoint')
list_objects = []

for file in my_bucket.objects.all():
    list_objects.append(file.key)

# print(list_objects.__len__() -1)
# print(list_objects[1])
# for obj in list_objects:
#     print(obj)

s3 = boto3.client('s3', aws_access_key_id='AKIA5RND2CEQZ7KOSO5T', aws_secret_access_key='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')
obj = s3.get_object(Bucket='di-aws-pinpoint', Key='ji2019/08/09/04/hello-1-2019-08-09-04-34-58-2c80cdfe-eb8c-4cd9-9846-1971e9ca6924')
data = (line.decode('utf-8') for line in obj['Body'].iter_lines())
date = ''
event = ''
Receipient = ''
Client_id = ''
i = 1
for row in data:
    data1 = json.loads(row)
    # print(data1)
    event = str(data1['event_type'])
    date = ''
    # print(event)
    if(event == '_email.open'):
        date = str(data1['facets']['email_channel']['mail_event']['mail']['headers'][0]['name'])
        date_value = str(data1['facets']['email_channel']['mail_event']['mail'] ['headers'][0]['value'])
        Receipient = str(data1['facets']['email_channel']['mail_event']['mail']['destination'][0])
        Client_id = str(data1['client']['client_id'])
        # item1 = {'Event': event, 'Id': Client_id, 'Address': Receipient}
        if(date == 'Date'):
            # thewriter.writerow(item1)
            actual_date = parse(date_value)
            # print('Date :', i, 'Event_type : ', event, ',', 'Receipient : ', Receipient, ',', 'Client_id : ', Client_id,
            #       ',','Date : ', datetime.strftime(actual_date,'%d-%m-%Y'))
            print('Date : ', date_value, ', ' , 'Actual_Date : ',datetime.strftime(actual_date,'%d-%m-%Y'))
            i = i + 1

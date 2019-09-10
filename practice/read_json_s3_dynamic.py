import boto3
import json
import csv
from datetime import datetime
from dateutil.parser import parse
session = boto3.Session(profile_name='praneeth')

# # data = {"HelloWorld": []}
# s3 = boto3.resource('s3')
# obj = s3.Object('diawspinpoint','ji2019/08/09/04/hello-1-2019-08-09-04-34-58-2c80cdfe-eb8c-4cd9-9846-1971e9ca6924')
# data = obj.get()['Body'].read().decode('utf-8')
# # print(data[209:236],' , ',data[848:869])
# for info in data:
#     print(data['event_type'])

s3 = session.resource('s3')
dynamodb=session.resource('dynamodb')
bucket_name = 'di-aws-pinpoint'
my_bucket = s3.Bucket(bucket_name)
list_keys = []

for file in my_bucket.objects.all():
    list_keys.append(file.key)

keys_list = list_keys.copy()
# i = 1
# for obj in list_keys:
#     print(i,obj)
#     i = i + 1
# keys_list.remove('ji2019/08/12/10/hello-1-2019-08-12-10-59-07-d1c8c5b4-3ada-4d66-a57a-cbeb58decaa7')
# keys_list.remove('ji2019/08/09/06/hello-1-2019-08-09-06-51-28-2dcf2389-3dc4-495f-8769-17b6ea6a6a2d')
# keys_list.remove('ji2019/08/08/12/hello-1-2019-08-08-12-01-03-e362c9e0-4d07-4f1e-9a80-9dae90179ba5')
# keys_list.remove('ji2019/08/08/11/hello-1-2019-08-08-11-50-29-c298acc6-b1a9-422b-967f-3efa6df001a9')
# keys_list.remove('success2019/08/06/07/analytics_to_s3-1-2019-08-06-07-11-07-1139d5ce-2059-4765-8506-f81fdd7f4eb0')
# j = 1
# for obj1 in keys_list:
#     print(j,obj1)
#     j = j + 1

s3 = boto3.client('s3', aws_access_key_id='AKIA5RND2CEQZ7KOSO5T', aws_secret_access_key='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')
i = 1
with open('C:/Users/nagraju/Desktop/writeData4.csv', 'a', newline='') as f:
    fieldnames = ['Event', 'Id', 'Address']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for keys in list_keys :
        # print(keys)
        obj = s3.get_object(Bucket=bucket_name, Key=keys)
        data = (line.decode('utf-8') for line in obj['Body'].iter_lines())

        date = ''
        date_value = ''
        event = ''
        Receipient = ''
        Client_id = ''
        for row in data:
            data1 = json.loads(row)
            # print(data1)
            event = str(data1['event_type'])
            date = ''
            # print(event)
            if(event == '_email.open' or event == '_email.click'):
                date = str(data1['facets']['email_channel']['mail_event']['mail']['headers'][0]['name'])
                date_value = str(data1['facets']['email_channel']['mail_event']['mail']['headers'][0]['value'])
                Receipient = str(data1['facets']['email_channel']['mail_event']['mail']['destination'][0])
                Client_id = str(data1['client']['client_id'])
                item1 = {'Event': event, 'Id': Client_id, 'Address': Receipient}
                if(date == 'Date'):
                    thewriter.writerow(item1)
                    actual_date = parse(date_value)
                    print('Sno :',i,'Event_type : ',event,'\t\t','Receipient : ',Receipient,'\t\t','Client_id : ',Client_id ,'\t\t',
                    'Date : ',datetime.strftime(actual_date,'%d-%m-%Y'))
                    i = i + 1


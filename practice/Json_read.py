import json
#File I/O Open function for read data from JSON File
with open('C:/Users/nagraju/Desktop/result_json.json') as file_object:
        # store file data in object

# sorted_string = json.dumps(data, indent=4, sort_keys=True)
# print(sorted_string.event_type)
 object = file_object.read()
 data = json.loads(object)
 print('Client_id : ', str(data['client']['client_id']))
 print('Receipient : ', str(data['facets']['email_channel']['mail_event']['mail']['destination'][0]))


import boto3
import json
s3 = boto3.client('s3')
object = s3.get_object(Bucket='diawspinpoint',Key='ji2019/08/09/05/hello-1-2019-08-09-05-00-43-8b367d5f-457b-432d-b53f-5a2218444135')
serializedObject = object['Body'].read()
# myData = json.loads(serializedObject)
print(serializedObject)
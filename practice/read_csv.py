# import csv
# with open('E:/Downloads/4edb2a71-733b-406d-b207-9c0332aca30e.csv','rt')as f:
#   data = csv.reader(f,skipinitialspace=True)
#   for row in data:
#     print(row[0],row[1])

# import pandas
# result = pandas.read_csv('E:/Downloads/4edb2a71-733b-406d-b207-9c0332aca30e.csv')
# print(result)

import boto3, csv
import pandas as pd

session = boto3.Session(profile_name='default')
s3_resource = session.resource('s3')

s3_object = s3_resource.Object(bucket_name='aws-athena-query-results-380315261948-us-east-1-di', key='Openers_data/2019/08/20/8eaeca17-2085-49e5-9862-14f990cdd99b.csv')

from io import StringIO

s3_data = StringIO(s3_object.get()['Body'].read().decode('utf-8'))

data = pd.read_csv(s3_data)
print(data)
# with open('C:/Users/nagraju/Desktop/writeData2.csv', mode='w') as file:
#  writer = csv.writer(file, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)
#  for row in pd.read_csv(s3_data):
#   print(row)
#   # writer.writerow(row)
import boto3
import os

def upload_file(path):
    session = boto3.Session(
        aws_access_key_id='AKIAVRDEOLP6JJCBXLUB',
        aws_secret_access_key='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',
        region_name='us-east-1'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('awsjsontest')

    with open(path, 'rb') as data:
                bucket.put_object(Key='some/path/to-s3/test1.csv', Body=data)
    # your s3 path will be /some/path/to-s3/test-x.csv
if __name__ == "__main__":
    upload_file('C:/Users/nagraju/Desktop/writeData5.csv')


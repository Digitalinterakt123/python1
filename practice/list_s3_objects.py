import logging
import boto3
from botocore.exceptions import ClientError


def list_bucket_objects(bucket_name):
    """List the objects in an Amazon S3 bucket

    :param bucket_name: string
    :return: List of bucket objects. If error, return None.
    """

    # Retrieve the list of bucket objects
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        # AllAccessDisabled error == bucket not found
        logging.error(e)
        return None
    return response['Contents']


def main():
    """Exercise list_bucket_objects()"""

    # Assign this value before running the program
    test_bucket_name = 'diawspinpoint'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the bucket's objects
    objects = list_bucket_objects(test_bucket_name)
    if objects is not None:
        # List the object names
        logging.info(f'Objects in {test_bucket_name}')
        for obj in objects:
           logging.info(f'  {obj["Key"]}')


if __name__ == '__main__':
    main()
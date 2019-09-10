import boto3
import json
session = boto3.Session(profile_name='praneeth')
client = session.client('pinpoint')
response = client.create_segment(
    ApplicationId='277007e5915041fdab0f147d5fd61114',
    WriteSegmentRequest={
        'Dimensions': {
            'Attributes': {

            },
            'Behavior': {

            },
            'Demographic': {

            },
            'Location': {

            },
            'Metrics': {

            },
            'UserAttributes': {

            }
        },
        'Name': 'AP_Api_Segment',
        'SegmentGroups': {
            'Groups': [
                {
                    'Dimensions': [
                        {
                            'Attributes': {

                            },
                            'Behavior': {

                            },
                            'Demographic': {

                            },
                            'Location': {

                            },
                            'Metrics': {

                            },
                            'UserAttributes': {
                                'state': {
                                    'AttributeType': 'INCLUSIVE',
                                    'Values': [
                                        'AP',
                                    ]
                                }
                            }
                        }
                    ],
                    'SourceSegments': [

                    ],
                    'SourceType': 'ANY',
                    'Type': 'ANY'
                },
            ],
            'Include': 'ALL'
        }
    }
)

# response = client.create_import_job(
#     ApplicationId='277007e5915041fdab0f147d5fd61114',
#     ImportJobRequest={
#         'Format': 'CSV',
#         'RoleArn': 'arn:aws:iam::930740834593:role/s3-pinpoint-admin',
#         'S3Url': 's3://di-pinpoint-python/Imports/test_ids',
#         'SegmentName': 'test_ids_import_python'
#
#     }
# )
print(json.dumps(response, indent=4, separators=(", ", " = ")))
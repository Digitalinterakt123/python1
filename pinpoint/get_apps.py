import boto3
import json

session = boto3.Session(profile_name='default')
client = session.client('pinpoint')
all_projects = client.get_apps()
# print(all_projects)
# print(json.dumps(all_projects, indent=4, separators=(", ", " = ")))
# print(all_projects['ApplicationsResponse']['Item']['Name'])

# For Geeting all the projects NAME and ID
for project in all_projects['ApplicationsResponse']['Item']:
    print('Id : ',project['Id'],'Project : ',project['Name'])
#
#     # For getting all the available campaigns
#     all_campaigns = client.get_campaigns(ApplicationId = project['Id'])
#     # print(json.dumps(all_campaigns, indent=4, separators=(", ", " = ")))
#     # print(all_campaigns['CampaignsResponse']['Item'])
#
#     for campaign in all_campaigns['CampaignsResponse']['Item']:
#          print('ApplicationId : ', campaign['ApplicationId'],'Campaign_Id : ',campaign['Id'],'Campaign_name : ',campaign['Name'])

# all_segments = client.get_segments(ApplicationId = 'a5b354c17c9643bb8a6f9aeb892c8304')
# print(json.dumps(all_segments, indent=4, separators=(", ", " = ")))

# for segment in all_segments['SegmentsResponse']['Item']:
#     print('segment_id : ',segment['Id'],'Segment_name : ',segment['Name'])
# segment = client.get_segment(ApplicationId = 'a5b354c17c9643bb8a6f9aeb892c8304',SegmentId = 'b5a15d07785946b5a7d85da4b9543ad7')
# print(json.dumps(segment, indent=4, separators=(", ", " = ")))
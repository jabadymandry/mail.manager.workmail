import boto3
region = 'us-east-1'
session = boto3.Session(profile_name="WORKMAIL", region_name=region)
client = session.client('workmail')
client.list_organizations()['OrganizationSummaries']
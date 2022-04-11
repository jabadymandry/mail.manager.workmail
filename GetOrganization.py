import boto3

session = boto3.Session(profile_name="WORKMAIL", region_name=regions[0])
client = session.client('workmail')
client.list_organizations()['OrganizationSummaries']
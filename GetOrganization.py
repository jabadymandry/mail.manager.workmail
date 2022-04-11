def GetOrganizationInfo(p="Id"):
    import boto3, os
    region = 'us-east-1'
    data = []
    session = boto3.Session(aws_access_key_id=os.getenv('Secret_USR'),
                                     aws_secret_access_key=os.getenv('Secret_PSW'),
                                     region_name=os.getenv('AwsRegion'))
    client = session.client('workmail')
    for info in client.list_organizations()['OrganizationSummaries']:
        if p == "Id":
            data.append(info['OrganizationId'])
        if p == "Domain":
            data.append(info['DefaultMailDomain'])
    return data

GetOrganizationInfo(p="Domain")
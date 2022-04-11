def GetOrganizationInfo(p="Id"):
    import boto3
    region = 'us-east-1'
    data = []
    session = boto3.Session(profile_name="WORKMAIL", region_name=region)
    client = session.client('workmail')
    for info in client.list_organizations()['OrganizationSummaries']:
        if p == "Id":
            data.append(info['OrganizationId'])
        if p == "Domain":
            data.append(info['DefaultMailDomain'])
    return data

GetOrganizationInfo(p="Domain")
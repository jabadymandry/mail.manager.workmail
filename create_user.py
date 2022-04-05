import boto3
import csv
from pass_gen import GenPass
import varsfile
import send_email

# Envoi email via SMTP SSL avec authentification. 
# Pensez à enseigner les variables d'environnement systèmes ci-après
# - SMTP_SERVER=smtp.xxxx.xxx
# - SMTP_PORT=xxx
# - SMTP_USER=xxxx@xxxxxx.xx
# - SMTP_PASS=xxxxxxxxx


def CreateMailAddress(file):
    session = boto3.Session(profile_name=varsfile._Env)
    workmail_client = session.client('workmail')
    with open(file, newline='') as csv_file:
        # Format CSV: DisplayName,NewEmail,OldEmail
        csv_data = csv.reader(csv_file, delimiter=';')
        for d in csv_data:
            password = GenPass()
            try:
                response = workmail_client.create_user(
                                OrganizationId= varsfile._OrganizationId,
                                Name=d[1],
                                DisplayName=d[0] if len(d[0]) > 0 else d[1],
                                Password=password,
                            )
                if(response['ResponseMetadata']['HTTPStatusCode'] == 200):
                    print("{0}: -> {1}@{2} / {3}".format(d.index(d[1]), d[1], varsfile._DomainName, password))
                    if(len(d[2]) > 0):
                        send_email.SendEmailInfo("{0}@{1}".format(d[1], varsfile._DomainName), password, d[2], varsfile._SenderMailAddress)
                    else:
                        print("{0} nouvel adresse email".format(d[1]))

            except workmail_client.exceptions.NameAvailabilityException:
                print("/!\ Compte e-mail  \"{0}@{1}\" existe deja!".format(d[1], varsfile._DomainName))
                pass


CreateMailAddress(varsfile._MailAddressFile)
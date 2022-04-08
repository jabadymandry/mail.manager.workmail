import os
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

class ManageEmail():
    def __init__(self):
        self.session = boto3.Session(aws_access_key_id=os.getenv('Secret_USR'),
                                     aws_secret_access_key=os.getenv('Secret_PSW'),
                                     region_name=os.getenv('AwsRegion'))
        self.workmail_client = self.session.client('workmail')
        self.fic = None
        self._OrganizationId = os.getenv('OrganisationId')
        self._DomainName = os.getenv('DomainName')

    def CreateMailAddress(self, verbose = False, save = True):
        """
        Création adresse email sur AWS Workmail depuis la liste CSV
        """
        if(save):
            self.fic = open(varsfile._MailInfoFile, "w")
            self.fic.write("Email;mot de passe\n")

        with open(varsfile._MailAddressFile, newline='') as csv_file:
            # Format CSV: DisplayName,NewEmail,OldEmail
            csv_data = csv.reader(csv_file, delimiter=',')
            for d in csv_data:
                password = GenPass()
                try:
                    response = self.workmail_client.create_user(
                                    OrganizationId= self._OrganizationId,
                                    Name=d[1],
                                    DisplayName=d[0] if len(d[0]) > 0 else d[1],
                                    Password=password,
                                )

                    if(response['ResponseMetadata']['HTTPStatusCode'] == 200):
                        self.EnableUser(self._OrganizationId, response['UserId'], d[1])
                        print("{0}: -> {1}@{2} / {3}".format(csv_data.line_num, d[1], self._DomainName, password))
                        if(len(d[2]) > 0):
                            send_email.SendEmailInfo("{0}@{1}".format(d[1], self._DomainName), password, d[2], varsfile._SenderMailAddress)
                        else:
                            if(verbose):
                                print(response)
                                print("{0} nouvel adresse email".format(d[1]))
                        
                    if(save == True):
                        data = "{0}@{1};{2}\n".format(d[1], self._DomainName, password)
                        self.SaveToFile(data)
                except self.workmail_client.exceptions.NameAvailabilityException:
                    print("/!\ Compte e-mail  \"{0}@{1}\" existe deja!".format(d[1], self._DomainName))
                    pass


    def EnableUser(self, _OrganizationId, _EntityId, _Email, verbose = True):
        """
        Activation compte email après création.
        Parametres:
            - OrganizationId
            - EntityId
            - Email
        """
        reponse = self.workmail_client.register_to_work_mail(
            OrganizationId = _OrganizationId,
            EntityId = _EntityId,
            Email = "{0}@{1}".format(_Email,self._DomainName)
            )
        if(verbose == True):
            if(reponse['ResponseMetadata']['HTTPStatusCode'] == 200):
                print("(i) - Activation {0} : [OK]".format(_Email))
            else:
                print("/!\ - Activation {0} : [KO]".format(_Email))
    
    def SaveToFile(self, _Data, verbose = False):
        """
        Sauvegarde emails info (login/password) dans fichiers
        """
        if(verbose):
            print("{0}\n".format(_Data))
        self.fic.write(_Data)


email = ManageEmail()
email.CreateMailAddress()
email.fic.close()
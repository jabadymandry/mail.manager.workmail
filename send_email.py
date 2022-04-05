import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import imaplib
import time
import varsfile

_Code_connexion_successful = 235

def TestConnect2MailServer(verbose = False, debug = False):
    """
    
    """
    try:
        with smtplib.SMTP_SSL(varsfile._SMTP_SERVER, varsfile._SMTP_PORT) as client_mail:
                # Create the client_mail connection
                client_mail.connect(host=varsfile._SMTP_SERVER, port=varsfile._SMTP_PORT)
                client_mail.ehlo()
                if(verbose == True and debug == True):
                    print("Connexion en cours, username: {0} / password: {1}".format(varsfile._SenderMailAddress, os.getenv('SMTP_PASS')))
                elif (verbose == True):
                    print("Connexion en cours, username: {0} / password: {1}".format(varsfile._SenderMailAddress, "*********************"))

                # Authenticate with the client_mail
                return client_mail.login(varsfile._SenderMailAddress, os.getenv('SMTP_PASS'))
    except Exception as err:
        print("Erreur de connexion au serveur: {0}".format(err))



def SendEmailInfo(_NewMailAddress, _NewPassword, _ToMailAddress, _SenderMailAddress="noreply@prodigy.gov.mg"):
    """

    """
    if ( TestConnect2MailServer()[0] == _Code_connexion_successful ):
        # Create message object instance
        msg = MIMEMultipart()
        
        # Create message body
        message = varsfile._CorpEmail.format(
            _NewMailAddress,
            _NewPassword,
            varsfile._SMTP_SERVER,
            varsfile._SMTP_PORT,
            varsfile._IMAP_SERVER,
            varsfile._IMAP_PORT,
            varsfile._WebMail
        )

        # Declare message elements
        msg['From'] = _SenderMailAddress
        msg['To'] = _ToMailAddress
        msg['Subject'] = "[BIENVENUE] - VOTRE MAIL {0}".format(varsfile._DomainName)

        # Add the message body to the object instance
        msg.attach(MIMEText(message, 'plain'))

        try:
            print("Envoie email en cours ...")
            with smtplib.SMTP_SSL(varsfile._SMTP_SERVER, varsfile._SMTP_PORT) as client_mail:
                # Create the client_mail connection
                client_mail.connect(host=varsfile._SMTP_SERVER, port=varsfile._SMTP_PORT)
                client_mail.ehlo()
                # Authenticate with the client_mail
                client_mail.login(varsfile._SenderMailAddress, os.getenv('SMTP_PASS'))
                # Send the message
                client_mail.sendmail(msg['From'], msg['To'], msg.as_string())
            print ("Successfully sent email to: {0}".format(msg['To']))
        except Exception as err:
            print("Une erreur s\'est produite pendant envoie de l\'e-mail: {0}".format(err))

        try:
            with imaplib.IMAP4_SSL(varsfile._IMAP_SERVER, varsfile._IMAP_PORT) as imap:
                imap.login(varsfile._SenderMailAddress, os.getenv('SMTP_PASS'))
                result = imap.append('"Sent Items"', '', imaplib.Time2Internaldate(time.time()), msg.as_string().encode('utf8'))
            print(result)
        except Exception as err:
            print("Une erreur s\'est produite pendant enregistrement de l\'e-mail: {0}".format(err))

#SendEmailInfo("bruno@prodigy.gov.mg", "sfsfsxxqKDs", "bruno@digital.gov.mg", "bruno@prodigy.gov.mg")
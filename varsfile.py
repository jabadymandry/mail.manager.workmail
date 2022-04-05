_OrganizationId='m-c5593a91faa84f8cad7721c01b0f4b90'
_DomainName='prodigy.gov.mg'
_MailAddressFile='emails.csv'
_Env='WORKMAIL'
_SenderMailAddress='bruno@prodigy.gov.mg'
_WebMail='https://prodigy-gov-mg.awsapps.com/mail '
_SMTP_SERVER='smtp.mail.us-east-1.awsapps.com'
_SMTP_PORT='465'
_IMAP_SERVER='imap.mail.us-east-1.awsapps.com'
_IMAP_PORT='993'

_CorpEmail = """\
    Bonjour,\n
        Je vous prie de trouver ci-dessous les informations relatif à votre nouvel adresse e-mail.\n
    \t\te-mail: {0} / mot de passe: {1}
    \t\tAccès webmail: {6}
    
    \t\Paramètre pour client mail:
    \t\tServeur sortant (SMTP): {2} / Port: {3}
    \t\tServeur entrant (IMAP): {4} / Port: {5}


    \t\tGuide utilisateur configuration client: 
    \t\t\t MS Outlook :  https://docs.aws.amazon.com/workmail/latest/userguide/outlook-client.html
    \t\t\t Mobile device): https://docs.aws.amazon.com/workmail/latest/userguide/mobile-client.html
    \t\t\t IMAP: https://docs.aws.amazon.com/workmail/latest/userguide/using_IMAP.html
    \t\t\t MacOS Mail App: https://docs.aws.amazon.com/workmail/latest/userguide/connect_mac_mail.html
        
        Vous pouvez désormais accéder, tester et/ou utiliser votre compte depuis le webmail (url ci-dessus) ou depuis votre client mail favoris.
        Nous vous invitons également de modifier votre mot de passe. Cela peut être fait à partir du webmail.

    Pour plus d'information veillez contacter votre administrateur.
    A votre service!
    --
    Message automatique\n
    MAIL SYSTEM
    """
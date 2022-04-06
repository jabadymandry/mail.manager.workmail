pipeline {
    agent any
    options {
        ansiColor('xterm')
    }

    parameters {
        string(name: 'OrganisationId', defaultValue: 'm-c5593a91faa84f8cad7721c01b0f4b90', description: '* Id organisation workmail, recupérer dans la console')
        string(name: 'DomainName', defaultValue: '', description: '* Nom de dommaine exemple: digital.gov.mg')
        //string(name: 'SenderEmail', defaultValue: 'mailman@${DomainName}', description: 'Adresse expediteur des infos du compte')
        string(name: 'AwsProfile', defaultValue: 'Default', description: 'Profile à utiliser pour se connecter sur AWS')
        string(name: 'UserToCreate', defaultValue: '', description: 'Utilisateur(s) à créer format csv FullName,User,Email-to-send-info')
        string(name: 'Group', defaultValue: '', description: 'Asso')
        booleanParam(name: 'AddToGroup', defaultValue: true, description: 'Check to confirm adding user to group below')

    }
    
    environment {
         SMTP_PASS  = credentials('d72d9067-293f-4261-827b-dc7679fdf9fb')
         GroupAll   = ""
         SenderEmail = "mailman@${DomainName}"
    }

    stages {
        stage('Create email') {
            steps {
                echo "Generate password for ${UserToCreate}"
            }
            steps {
                echo "Creating ${UserToCreate} email address"
            }
            steps {
                echo "Creating ${UserToCreate} email address"
            }
        }

        stage('Add to group') {
            when {
                expression {
                    params.AddToGroup
                }
            }

            steps {
                echo "Adding ${UserToCreate} to group ${Group}"
            }
        }

        stage('Send email') {
            steps {
                echo "Sending email"
            }
        }
    }

/*    post {
        always {
            archiveArtifacts artifacts: "${env.WORKSPACE}/terraform/tfplan.txt"
        }
    }*/
}
pipeline {
    agent any
    options {
        ansiColor('xterm')
    }

    parameters {
        string(name: 'OrganisationId', defaultValue: 'm-c5593a91faa84f8cad7721c01b0f4b90', description: '* Unique ID organisation on workmail')
        string(name: 'DomainName', defaultValue: '', description: '* - Domain name ex: prodigy.gov.mg')
        string(name: 'AwsProfile', defaultValue: 'Default', description: 'AWS profile name to use')
        string(name: 'FullName', defaultValue: '', description: '* - Full name do display for email address')
        string(name: 'EmailToCreate', defaultValue: '', description: '* - Email address to create')
        string(name: 'SendInfoToEmail', defaultValue: '', description: '* - Send email information (email/password) to mailbox')
        string(name: 'Group', defaultValue: '', description: 'Ajouter au groupe')
        booleanParam(name: 'AddToGroup', defaultValue: true, description: 'Check to confirm adding user to group below')

    }
    
    environment {
         SMTP_PASS  = credentials('')
         GroupAll   = ""
         SenderEmail = "mailman@${DomainName}"
    }

    stages {
        stage('Create email') {
            steps {
                script {
                    File file = new File("emails.csv")
                    file.write "${FullName},${EmailToCreate},${SendInfoToEmail}" 
                    println file.text
                    sh 'python3 create_user.py'
                }
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
    }

/*    post {
        always {
            archiveArtifacts artifacts: "${env.WORKSPACE}/terraform/tfplan.txt"
        }
    }*/
}
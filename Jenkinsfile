pipeline {
    agent none
    
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
        GroupAll   = ""
        SenderEmail = "mailman@${DomainName}"
        Secret = credentials('168d1e6b-0697-4f33-ada2-4b9f61dcecd8')
        SMTP_PASS = credentials('0dbee823-44c5-4e66-8297-92e3fd3c53da')
    }

    stages {
        stage('Create email') {
            agent{
                docker { 
                    image 'demisto/boto3py3:1.0.0.28264' 
                    label 'force-ci'
                    reuseNode true
                    //args "-e ${Secret_USR} -e ${Secret_PSW}"
    
                }
            }
            steps {
                echo "${Secret}"
                echo "${FullName},${EmailToCreate},${SendInfoToEmail}"
                script {
                    writeFile file:'emails.csv', text:"${FullName},${EmailToCreate},${SendInfoToEmail}"
                }
                //sh 'apt-get update && apt-get install python3-pip -y && python3 -m pip install boto3'
                sh 'printenv'
                sh 'python3 create_user.py'
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
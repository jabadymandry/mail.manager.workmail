pipeline {
    agent none
    
    environment{
        Secret = credentials('168d1e6b-0697-4f33-ada2-4b9f61dcecd8')
        AwsRegion = 'us-east-1'
    }


    stages {
        stage('Check variable'){
            agent {
                docker { 
                    image 'demisto/boto3py3:1.0.0.28264' 
                    label 'forge-ci'
                    reuseNode true
                    //args "-e ${Secret_USR} -e ${Secret_PSW}"
                }
            }
            steps {
                script{
                    sh 'ip addr show'
                    sh 'python3 GetOrganization.py'
                }

            }
        }
    }
}
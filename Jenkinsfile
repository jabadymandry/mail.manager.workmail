pipeline {
    agent any
    stages {
        stage('Check variable'){
            agent {
                label 'forge-ci'
            }
            steps {
                script{
                    sh 'python GetOrganization.py'
                }

            }
        }
    }
}
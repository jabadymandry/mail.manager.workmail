def result

pipeline {
    agent none
    
    environment{
        Secret = credentials('168d1e6b-0697-4f33-ada2-4b9f61dcecd8')
        AwsRegion = 'us-east-1'
    }

    parameters {
        string(name: 'FullName', defaultValue: '', description: '* - Full name do display for email address')
        string(name: 'EmailToCreate', defaultValue: '', description: '* - Email address to create')
        string(name: 'SendInfoToEmail', defaultValue: '', description: '* - Send email information (email/password) to mailbox')
        string(name: 'Group', defaultValue: '', description: 'Ajouter au groupe')
        booleanParam(name: 'AddToGroup', defaultValue: false, description: 'Check to confirm adding user to group below')

    }
    stages {
        stage('Init variables'){
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
                    result = sh (script: 'python3 GetOrganization.py', returnStdout: true)
                    echo "${result}"
                    properties([
                        parameters([
                            [$class: 'ChoiceParameter', 
                            choiceType: 'PT_SINGLE_SELECT', 
                            description: 'Select the Environemnt from the Dropdown List', 
                            filterLength: 1, 
                            filterable: false, 
                            name: 'DomainName', 
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        "return['Could not get The environemnts']"
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        "return ${result}"
                                ]
                            ]
                            ],
                            [$class: 'CascadeChoiceParameter', 
                                choiceType: 'PT_SINGLE_SELECT', 
                                description: 'Organisation Id Workmail',
                                name: 'Organization_Id', 
                                referencedParameters: 'DomainName', 
                                script: 
                                    [$class: 'GroovyScript', 
                                    fallbackScript: [
                                        classpath: [], 
                                        sandbox: false, 
                                        script: "return['Could not get Organization Id']"
                                    ], 
                                script: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: '''
                                        if (DomainName.equals("digital.gov.mg")){
                                            return["m-35959561b27a4d4b8408a9fe2f5daba4"]
                                        }
                                        else if(DomainName.equals("prodigy.gov.mg")){
                                            return["m-c5593a91faa84f8cad7721c01b0f4b90"]
                                        }
                                        else if(DomainName.equals("cirt.gov.mg")){
                                            return["m-40067b6aa0cc44a6b8bad1b8a7a50985"]
                                        }
                                        else if(DomainName.equals("mndpt.gov.mg")){
                                            return["m-deff13a8a7ff436dbc7ad38a690f861e"]
                                        }
                                        else if(DomainName.equals("commune.gov.mg")){
                                            return["m-6c38bcb78baf426b8757cdc57c977f99"]
                                        }         
                                        '''
                                    ] 
                                ]
                            ],

                        ])
                    ])
                }
            }
        }
        stage('Create email'){
            steps{
                echo "${DomainName} ,${Organisation_Id}"
                echo "${FullName},${EmailToCreate},${SendInfoToEmail}"
                script {
                    writeFile file:'emails.csv', text:"${FullName},${EmailToCreate},${SendInfoToEmail}"
                }
            }
        }
    }
}
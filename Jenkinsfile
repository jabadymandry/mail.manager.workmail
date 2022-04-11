properties([
  parameters([
    [
      $class: 'ChoiceParameter',
      choiceType: 'PT_SINGLE_SELECT',
      name: 'DomainName',
      script: [
        $class: 'ScriptlerScript',
        scriptlerScriptId:'script.groovy'
      ]
    ],
    [
      $class: 'CascadeChoiceParameter',
      choiceType: 'PT_SINGLE_SELECT',
      name: 'ConfigValue',
      referencedParameters: 'DomainName',
      script: [
        $class: 'ScriptlerScript',
        scriptlerScriptId:'servicemailinfo.groovy',
        parameters: [
          [name:'DomainName', value: '$D']
        ]
      ]
   ]
 ])
])

pipeline {
    agent none

    environment {
        GroupAll   = ""
        SenderEmail = "mailman@${DomainName}"
        Secret = credentials('168d1e6b-0697-4f33-ada2-4b9f61dcecd8')
        SMTP_PASS = credentials('0dbee823-44c5-4e66-8297-92e3fd3c53da')
        SenderEmailAddress = 'bruno@prodigy.gov.mg'
        Organisation_Id = 'm-c5593a91faa84f8cad7721c01b0f4b90'
        DomainName = 'prodigy.gov.mg'
        AwsRegion = 'us-east-1'
    }




    stages {
        stage('Initialisation'){
            steps{
                echo "${params.DomainName}"
                echo "${params.ConfigValue}"
            }
        }
/*         stage('Create email') {
            agent{
                docker { 
                    image 'demisto/boto3py3:1.0.0.28264' 
                    label 'force-ci'
                    reuseNode true
                    //args "-e ${Secret_USR} -e ${Secret_PSW}"
    
                }
            }
            steps {
                //echo "${Organisation_Id}"
                //echo "${FullName},${EmailToCreate},${SendInfoToEmail}"
                script {
                    writeFile file:'emails.csv', text:"${FullName},${EmailToCreate},${SendInfoToEmail}"
                }
                //sh 'printenv'
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
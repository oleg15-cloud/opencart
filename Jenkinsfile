pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
        stage('Test') {
            steps {
                sh '/var/jenkins_home/.local/bin/pytest -v tests -n${NUMBER} --url ${URL} --executor ${EXECUTOR} --browser_name ${BROWSER_NAME} --bversion ${BROWSER_VERSION}'
            }
        }
    }

    post {

        always {

            script {
                allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                ])
            }

            cleanWs()
        }
    }
}
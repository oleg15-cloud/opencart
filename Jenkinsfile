pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh '/var/jenkins_home/.local/bin/pytest -v tests --browser ${BROWSER_NAME} --bversion ${BROWSER_VERSION}'
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
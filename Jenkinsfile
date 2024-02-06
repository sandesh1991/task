pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'npprod:latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '/usr/local/bin/docker build -t npprod:latest .'
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    sh '/usr/local/bin/docker run --name npprod-container -d ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            echo 'Test Test Test'
        }
        success {
            echo 'Pipeline Run Successfull'
        }
        failure {
            echo 'Pipeline Run failed'
        }
    }
}


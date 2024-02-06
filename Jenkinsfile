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

        stage('Test Cases') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'venv/bin/pip install numpy pytest'
                    sh 'venv/bin/pip list'
                    sh 'venv/bin/python3 -m pytest -v'
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    // Stop and remove previous container named npprod-container
                    sh '/usr/local/bin/docker stop npprod-container || true'
                    sh '/usr/local/bin/docker rm npprod-container || true'
                    // Build a new container
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


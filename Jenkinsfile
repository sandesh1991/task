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
                    docker.build("${env.DOCKER_IMAGE}").inside {
                    }
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").run()
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


pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'npprod:latest'
    }
    stages {
        stage('Build docker image for ') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").run()
                }
            }
        }
    }
}

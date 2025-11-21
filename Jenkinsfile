
pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'vamsikpdevops'  // Your Docker Hub username
        IMAGE_NAME = 'devops-mini'
        IMAGE_TAG = 'latest'  // Can be 'latest', '1.0', etc.
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image with correct tag
                    docker.build("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Use your actual Jenkins credentials ID here
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Clean Up Local Images') {
            steps {
                script {
                    // Remove dangling images to save space
                    sh 'docker system prune -f'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}

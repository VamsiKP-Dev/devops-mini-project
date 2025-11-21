
pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'vamsikpdevops'  // Your Docker Hub username
        IMAGE_NAME = 'devops-mini'
        IMAGE_TAG = 'latest'  // Can also use a version number
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
                    // Build Docker image
                    docker.build("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Use the correct Jenkins credentials ID for Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', 'flask-calc-ci-cd') {
                        docker.image("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Clean Up Local Images') {
            steps {
                script {
                    // Remove unused Docker images to free space
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

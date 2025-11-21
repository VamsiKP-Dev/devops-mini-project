
pipeline {
    agent any

    environment {
        IMAGE_NAME = "vamsikpdevops/devops-mini"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/VamsiKP-Dev/devops-mini-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'docker-hub-credentials1.1',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        echo "Logging in to Docker Hub..."
                        bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                        echo "Pushing Docker image..."
                        bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Clean Up Local Images') {
            steps {
                script {
                    echo "Removing local Docker images..."
                    bat "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || echo 'Image not found, skipping cleanup.'"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}


pipeline {
    agent any

    environment {
        IMAGE_NAME = "vamsikpdevops/devops-mini:latest"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                        bat "docker push %IMAGE_NAME%"
                    }
                }
            }
        }

        stage('Clean Up Local Images') {
            steps {
                script {
                    bat "docker rmi %IMAGE_NAME% || echo Image not found, skipping cleanup"
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

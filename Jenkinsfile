
pipeline {
    agent any

    environment {
        IMAGE = "${env.DOCKER_HUB_USER}/devops-mini:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm $IMAGE python -m pytest -q'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_HUB_USER',
                    passwordVariable: 'DOCKER_HUB_PASS'
                )]) {
                    sh 'echo $DOCKER_HUB_PASS | docker login -u $DOCKER_HUB_USER --password-stdin'
                    sh 'docker push $IMAGE'
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                // Deploy using Kubernetes
                sh 'kubectl set image deployment/devops-mini devops-mini=$IMAGE --record || true'
                sh 'kubectl apply -f k8s/'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}


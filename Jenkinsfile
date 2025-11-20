
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
     withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
       sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
       sh 'docker push $IMAGE'
    }
  }
}
stage('Deploy to K8s') {
  steps {
// Assumes kubeconfig is available on Jenkins node or via credentials
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
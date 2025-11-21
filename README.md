---

# ✅ **FINAL README.md (Copy–Paste Directly)**

```markdown
# 🧮 DevOps Mini Project – Flask Calculator API

<p align="center">

  <!-- Build Status (Jenkins badge static, because local Jenkins is not public) -->
  <img src="https://img.shields.io/badge/Jenkins-Build%20Passing-brightgreen?style=for-the-badge&logo=jenkins" />

  <!-- Docker Pulls -->
  <a href="https://hub.docker.com/r/vamsikpdevops/devops-mini">
    <img src="https://img.shields.io/docker/pulls/vamsikpdevops/devops-mini?style=for-the-badge&logo=docker" />
  </a>

  <!-- Docker Image Size -->
  <img src="https://img.shields.io/docker/image-size/vamsikpdevops/devops-mini/latest?style=for-the-badge&logo=docker" />

  <!-- GitHub Stars -->
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/stargazers">
    <img src="https://img.shields.io/github/stars/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>

  <!-- GitHub Forks -->
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/forks">
    <img src="https://img.shields.io/github/forks/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>

  <!-- GitHub Issues -->
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/issues">
    <img src="https://img.shields.io/github/issues/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>

  <!-- Last Commit -->
  <img src="https://img.shields.io/github/last-commit/VamsiKP-Dev/devops-mini-project?style=for-the-badge&logo=git" />

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />

  <!-- Flask -->
  <img src="https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask" />

  <!-- Kubernetes -->
  <img src="https://img.shields.io/badge/Kubernetes-Ready-blue?style=for-the-badge&logo=kubernetes" />

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />

</p>

---

## 📘 Project Overview

This project is a **Dockerized Flask Calculator API** with:

✅ Automatic CI/CD pipeline using **Jenkins**  
✅ Docker image build + push to **DockerHub**  
✅ Automated testing with **pytest**  
✅ Deployment to **Kubernetes** (kubectl apply)  
✅ REST API for arithmetic operations  

This project demonstrates **end-to-end DevOps workflow**.

---

## 🏗️ Project Structure

```

devops-mini-project/
│── app/
│   ├── app.py
│   ├── calculator.py
│── tests/
│   ├── test_app.py
│── Dockerfile
│── requirements.txt
│── Jenkinsfile
│── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
└── README.md

```

---

## 🚀 Features

- REST API built using Flask  
- Supports operations: **add, sub, mul, div**  
- Dockerized for consistent deployment  
- Automated CI/CD pipeline  
- Unit-Tested  
- Kubernetes Deployment Ready  

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|-------|----------|-------------|
| GET | `/` | Health message |
| GET | `/health` | Service health check |
| GET | `/calc?op=add&a=10&b=20` | Perform calculation |

### Example usage:

```

[http://localhost:5000/calc?op=add&a=10&b=5](http://localhost:5000/calc?op=add&a=10&b=5)

````

Response:

```json
{
  "Result": 15
}
````

---

## 🐳 Docker Instructions

### **Build image**

```sh
docker build -t devops-mini .
```

### **Run container**

```sh
docker run -p 5000:5000 devops-mini
```

### DockerHub Image

👉 [https://hub.docker.com/r/vamsikpdevops/devops-mini](https://hub.docker.com/r/vamsikpdevops/devops-mini)

---

## 🧪 Run Tests

```sh
pytest -q
```

---

## ⚙️ Jenkins CI/CD Pipeline

Your pipeline includes:

* **Checkout code**
* **Build Docker image**
* **Run tests**
* **Push image to DockerHub**
* **Deploy to Kubernetes**

### Jenkinsfile used:

```groovy
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
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials1.1', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
          sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
          sh 'docker push $IMAGE'
        }
      }
    }

    stage('Deploy to K8s') {
      steps {
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
```

---

## ☸️ Kubernetes Deployment

Apply all manifests:

```sh
kubectl apply -f k8s/
```

Check pod:

```sh
kubectl get pods
```

Access service:

```sh
kubectl get svc
```

---

## 👨‍💻 Author

**Vamsi Krishna**
DevOps Engineer | Cloud | Automation | CI/CD

GitHub: [https://github.com/VamsiKP-Dev](https://github.com/VamsiKP-Dev)

---

## 📄 License

MIT License – feel free to use and extend.

---

# 🎉 Done!

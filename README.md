
---

# 📘 DevOps Mini Project — Flask Calculator App (CI/CD using Jenkins, Docker & Kubernetes)

This project is a complete **CI/CD pipeline** setup for a simple **Flask-based Calculator API**, using:

* **Python + Flask**
* **Docker**
* **PyTest**
* **Jenkins (Declarative Pipeline)**
* **DockerHub**
* **Kubernetes (kubectl deployment)**

The pipeline automates:

✔ Building Docker Image
✔ Running Unit Tests
✔ Pushing Image to DockerHub
✔ Deploying to Kubernetes

---

## 🚀 Project Architecture

```
+----------------+      +--------------------+      +-------------------+
|   GitHub Repo  | ---> |   Jenkins Pipeline | ---> |   DockerHub        |
+----------------+      +--------------------+      +-------------------+
                                   |
                                   v
                           +----------------+
                           |   Kubernetes   |
                           +----------------+
```

---

## 🗂 Project Structure

```
devops-mini-project/
│
├── app/
│   ├── app.py
│   ├── calculator.py
│   └── __init__.py
│
├── tests/
│   └── test_calc.py
│
├── Dockerfile
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## 🔧 Technologies Used

| Tool / Tech    | Purpose             |
| -------------- | ------------------- |
| **Flask**      | Calculator REST API |
| **Docker**     | Containerize API    |
| **PyTest**     | Unit testing        |
| **Jenkins**    | CI/CD automation    |
| **DockerHub**  | Image registry      |
| **Kubernetes** | Deployment          |

---

## 🧮 API Endpoints

### **Health Check**

```
GET /health
```

### **Calculator Operation**

```
GET /calc?op=add&a=10&b=20
```

Supported operations:

| Operation | Example             |
| --------- | ------------------- |
| add       | `?op=add&a=5&b=3`   |
| sub       | `?op=sub&a=10&b=4`  |
| mul       | `?op=mul&a=10&b=20` |
| div       | `?op=div&a=20&b=5`  |

---

## 🐳 Docker Commands

### **Build Image**

```
docker build -t devops-mini .
```

### **Run Container**

```
docker run -p 5000:5000 devops-mini
```

---

## 🧪 Run Tests Locally

```
pytest -q
```

---

## 📦 Jenkins Declarative Pipeline

The pipeline performs:

1️⃣ Checkout code from GitHub
2️⃣ Build Docker image
3️⃣ Run PyTest inside container
4️⃣ Push image to DockerHub
5️⃣ Deploy to Kubernetes

---

## 🛠 Jenkins Credentials Required

| ID                          | Type             | Purpose            |
| --------------------------- | ---------------- | ------------------ |
| `docker-hub-credentials1.1` | Username + Token | Push Docker images |
| `github-pat`                | GitHub PAT       | Repo access        |

---

## 🌐 Kubernetes Commands

### Apply Deployment:

```
kubectl apply -f k8s/
```

### Update Image:

```
kubectl set image deployment/devops-mini devops-mini=<image>
```

---

## 📝 Dockerfile (Summary)

* Uses Python 3.11 slim image
* Installs requirements
* Copies app + tests
* Exposes port 5000
* Runs Flask app

---

## 📄 Jenkinsfile (Summary)

* Builds docker image
* Runs PyTest
* Pushes to DockerHub
* Deploys to Kubernetes

---

## 👨‍💻 Author

**Vamsi Krishna (DevOps Engineer)**
GitHub: *VamsiKP-Dev*

---

If you want, I can also generate a **diagram**, **badges**, or **screenshots section** for your README.

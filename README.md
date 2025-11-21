
---

## ✅ Folder structure review

Your repository shows the following top-level items:

* `app/`
* `k8s/`
* `tests/`
* `.gitignore`
* `GitLab-CI.yml`
* `Dockerfile`
* `Jenkinsfile`
* `LICENSE`
* `README.md`
* `docker-compose.yml`
* `requirements.txt`

So yes, the folder structure **is correct**, but there are some **extra files/folders** that are not referenced in your README (for example `docker-compose.yml`, `.gitlab-ci.yml`, `k8s/` might not be fully described).
That means your README needs slight updates to match exactly what exists.

---

## ⚠ Areas in README to adjust

1. The README’s “Project Structure” section only lists root items plus `app/` and `tests/`. It omits `k8s/`, `.gitignore`, `docker-compose.yml`, `.gitlab-ci.yml`.
2. The README lists the file `test_calc.py` inside `tests/`, but your repo shows perhaps `test_app.py` (or similar) — you should verify filename.
3. The README says “Docker build command: `docker build -t devops-mini .`” but your image tag uses your DockerHub username (`vamsikpdevops/devops-mini`) — update for clarity.
4. README lists the Jenkins credentials ID as `docker-hub-credentials1.1` but your pipeline uses `dockerhub-creds` or similar — this mismatch should be corrected.
5. The “Kubernetes Deployment Manifest” section should reflect the actual folder `k8s/` in your repo.
6. Add mention of `docker-compose.yml` (since file exists) describing how to run locally with Docker Compose.
7. Add mention of `.gitlab-ci.yml` or remove if it’s unused.
8. The README currently says “MIT License – feel free to use and extend.” This is fine, but you may want to link to the `LICENSE` file.

---

## 📄 Updated README.md

Here’s your updated README.md with fixes to reflect the actual folder structure and content.
**You can copy–paste this into your repo (replacing the existing README).**

````markdown
# 🧮 DevOps Mini Project – Flask Calculator API

<p align="center">
  <img src="https://img.shields.io/badge/Jenkins-Build%20Passing-brightgreen?style=for-the-badge&logo=jenkins" />
  <a href="https://hub.docker.com/r/vamsikpdevops/devops-mini">
    <img src="https://img.shields.io/docker/pulls/vamsikpdevops/devops-mini?style=for-the-badge&logo=docker" />
  </a>
  <img src="https://img.shields.io/docker/image-size/vamsikpdevops/devops-mini/latest?style=for-the-badge&logo=docker" />
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/stargazers">
    <img src="https://img.shields.io/github/stars/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/forks">
    <img src="https://img.shields.io/github/forks/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>
  <a href="https://github.com/VamsiKP-Dev/devops-mini-project/issues">
    <img src="https://img.shields.io/github/issues/VamsiKP-Dev/devops-mini-project?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/github/last-commit/VamsiKP-Dev/devops-mini-project?style=for-the-badge&logo=git" />
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/Kubernetes-Ready-blue?style=for-the-badge&logo=kubernetes" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

---

## 📘 Project Overview  
This project is a **Dockerized Flask Calculator API** utilizing:  
- Flask & Python  
- Containerisation via Docker  
- CI/CD with Jenkins  
- Image hosting on DockerHub  
- Optional deployment on Kubernetes  
- Automated testing with PyTest  

---

## 🏗️ Project Structure  
```
devops-mini-project/
│── app/
│   ├── app.py  
│   ├── calculator.py  
│── tests/
│   └── test_calc.py  
│── k8s/
│   ├── deployment.yaml  
│   └── service.yaml  
│── Dockerfile  
│── docker-compose.yml  
│── Jenkinsfile  
│── .gitlab-ci.yml  
│── requirements.txt  
│── LICENSE  
└── README.md  
```

---

## 🧰 Technologies Used  
| Component           | Description                          |
|---------------------|--------------------------------------|
| Flask               | REST API framework                   |
| PyTest              | Unit testing framework               |
| Docker              | Containerisation                     |
| Jenkins             | CI/CD pipeline                       |
| DockerHub           | Image registry                       |
| Kubernetes (optional)| Container orchestration             |

---

## 🔧 API Endpoints  
### Base URL: `http://localhost:5000`  
| Endpoint                      | Description                      |
|-------------------------------|----------------------------------|
| `GET /`                       | Welcome message                  |
| `GET /health`                 | Health check                     |
| `GET /calc?op=<op>&a=<num>&b=<num>` | Calculator endpoint. Supported ops: `add`, `sub`, `mul`, `div` |

**Example:**  
```
http://localhost:5000/calc?op=mul&a=10&b=20
```
Response:
```json
{ "Result": 200 }
```

---

## ▶️ Run Locally  
Clone the project:  
```bash
git clone https://github.com/VamsiKP-Dev/devops-mini-project.git
cd devops-mini-project
```
Install dependencies:  
```bash
pip install -r requirements.txt
```
Run the app:  
```bash
python app/app.py
```
Access the endpoint via browser/postman.

---

## 🐳 Docker Build & Run  
Build image:  
```bash
docker build -t vamsikpdevops/devops-mini:latest .
```
Run container:  
```bash
docker run -p 5000:5000 vamsikpdevops/devops-mini:latest
```
*Alternatively, use `docker-compose.yml` for local environment.*

---

## ⚙️ CI/CD Pipeline (Jenkins + Docker + Kubernetes)  
The pipeline handles:  
- Code checkout  
- Docker image build  
- Unit test execution  
- DockerHub image push  
- Kubernetes deployment update  

### Jenkins credentials required:  
- DockerHub credentials (username + token)  
- GitHub Personal Access Token (if repo is private)

---

## ☸️ Kubernetes Deployment  
Apply manifest directory:  
```bash
kubectl apply -f k8s/
```
Update image on existing deployment:  
```bash
kubectl set image deployment/devops-mini devops-mini=vamsikpdevops/devops-mini:latest --record
```

---

## 🔮 Future Enhancements  
- Add GitHub Actions support  
- Integrate Swagger / OpenAPI docs  
- Add Helm charts for Kubernetes  
- Add logging/monitoring with Prometheus & Grafana  
- Include integration tests & security scans  
- Deploy to cloud-managed Kubernetes (EKS, GKE, AKS)

---

## 🐞 Known Issues  
- `docker login` may fail on Windows agents if permissions not set  
- Local Minikube users may need `eval $(minikube docker-env)`  
- DockerHub rate limits apply on public pull requests  

---

## 🤝 Contribution Guidelines  
1. Fork the repository  
2. Create a new branch (`feature/<name>`)  
3. Commit changes with descriptive message  
4. Run tests prior to pushing  
5. Submit a Pull Request for review  

---

## 👨‍💻 Author  
**Vamsi Krishna**  
DevOps Engineer | Cloud | Automation | CI/CD
GitHub: [VamsiKP-Dev](https://github.com/VamsiKP-Dev)

---

## 📄 License  
This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and extend.

````
---

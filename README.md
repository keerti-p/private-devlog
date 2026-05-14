# 🚀 DevLog

### Flask + MySQL + Docker + Jenkins + AWS + Kubernetes + Terraform

A modern web application where users can log daily development activities, share updates, give kudos, and track productivity using dashboards, timelines, and statistics.

---

# 📌 Project Overview

DevLog is a full-stack Flask application integrated with MySQL and deployed using a complete DevOps workflow.

The project demonstrates:

* Full-stack web development
* Database integration
* Docker containerization
* Jenkins CI/CD automation
* AWS cloud deployment
* Kubernetes orchestration
* Terraform Infrastructure as Code

---

# 🌟 Features

✅ User Authentication
✅ Dashboard Activity Feed
✅ Timeline View
✅ Kudos / Like System
✅ Team Leaderboard
✅ Statistics Dashboard
✅ Dockerized Deployment
✅ Jenkins CI/CD Pipeline
✅ Kubernetes Deployment
✅ Terraform Infrastructure Provisioning

---

# 🛠 Tech Stack

| Category         | Technology            |
| ---------------- | --------------------- |
| Backend          | Python Flask          |
| Database         | MySQL                 |
| Frontend         | HTML, CSS, JavaScript |
| Containerization | Docker                |
| CI/CD            | Jenkins               |
| Orchestration    | Kubernetes            |
| Infrastructure   | Terraform             |
| Cloud            | AWS EC2               |
| Version Control  | Git & GitHub          |

---

# 📁 Project Structure

```bash id="k2d0hz"
devlog/
├── app.py                  ← Flask backend (all routes)
├── schema.sql              ← MySQL database + sample data
├── requirements.txt        ← Python packages
├── Dockerfile              ← Docker image for Flask app
├── docker-compose.yml      ← Runs Flask + MySQL together
├── Jenkinsfile             ← Jenkins CI/CD pipeline
├── terraform/              ← Terraform IaC files
├── k8s/                    ← Kubernetes manifests
└── templates/
    ├── base.html           ← Shared layout + sidebar
    ├── login.html          ← Login page
    ├── register.html       ← Register page
    ├── dashboard.html      ← Activity feed
    ├── post.html           ← Log new activity
    ├── timeline.html       ← Timeline grouped by date
    └── stats.html          ← Leaderboard + charts
```

---

# ⚙️ Local Setup

## Step 1 — Install MySQL

### Ubuntu/Linux

```bash id="i6x7ec"
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

### Mac

```bash id="jmfsyw"
brew install mysql
brew services start mysql
```

### Windows

Install MySQL Installer and start MySQL service.

---

## Step 2 — Configure Database

Login to MySQL:

```bash id="zjlwmk"
mysql -u root -p
```

Run schema file:

```sql id="7q2b9v"
source schema.sql;
```

Creates:

* Database → `devlog_db`
* User → `devlog_user`
* Password → `devlog_pass`

---

## Step 3 — Install Dependencies

```bash id="nwd6xy"
pip install -r requirements.txt
```

---

## Step 4 — Run Flask Application

```bash id="l9xxm4"
python app.py
```

Open in browser:

```bash id="fj7u7k"
http://localhost:5000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash id="69q5u2"
docker build -t devlog .
```

---

## Run Docker Container

```bash id="pbhl0d"
docker run -d -p 5000:5000 devlog
```

Open:

```bash id="6o6kj5"
http://localhost:5000
```

---

# 🧩 Docker Compose Setup

Docker Compose runs Flask and MySQL together.

## Start Containers

```bash id="r4iqf3"
docker compose up --build -d
```

---

## Useful Commands

```bash id="5z8mkm"
docker compose logs
docker compose down
docker compose down -v
docker ps
```

---

# ☁️ AWS EC2 Deployment

## Launch EC2 Instance

Open ports in Security Group:

* 22 → SSH
* 80 → HTTP
* 5000 → Flask App

---

## Connect to EC2

```bash id="b8s7ns"
ssh -i key.pem ubuntu@your-public-ip
```

---

## Pull Docker Image

```bash id="n0tt9x"
docker pull yourdockerhubusername/devlog:latest
```

---

## Run Application

```bash id="9t2u9k"
docker run -d -p 80:5000 yourdockerhubusername/devlog:latest
```

Access:

```bash id="i0km3w"
http://your-public-ip
```

---

# ☸️ Kubernetes Deployment

Inside `k8s/` folder:

## Deploy Resources

```bash id="r0b9zj"
kubectl apply -f .
```

---

## Verify Deployment

```bash id="0gfgn5"
kubectl get pods
kubectl get svc
kubectl get deployments
```

---

# 🏗 Terraform Infrastructure

Inside `terraform/` folder:

## Initialize Terraform

```bash id="w4ru3e"
terraform init
```

---

## Check Infrastructure Plan

```bash id="p74b6x"
terraform plan
```

---

## Create Infrastructure

```bash id="1alvmm"
terraform apply
```

---

## Destroy Infrastructure

```bash id="smxhfy"
terraform destroy
```

---

# 🔄 Jenkins CI/CD Pipeline

The project uses Jenkins to automate the software delivery process from source code checkout to deployment.

---

# 🖥 Jenkins Infrastructure Setup

## Jenkins Master Node

A dedicated EC2 instance was configured as Jenkins Master.

Installed Components:

* Java
* Jenkins
* Docker

Responsibilities:

* Manage Jenkins jobs
* Trigger CI/CD pipelines
* Connect with GitHub repository
* Manage slave agents
* Monitor build execution

---

## Jenkins Slave Node

A separate EC2 instance was configured as Jenkins Slave Node.

Installed Components:

* Java
* Docker
* Python
* Python dependencies

Responsibilities:

* Execute pipeline stages
* Run application tests
* Build Docker images
* Push images to Docker Hub
* Deploy application

The slave node was attached to the Jenkins Master using Jenkins agent configuration.

---

# ⚡ Detailed Jenkins Pipeline Workflow

The Jenkins pipeline automates the complete DevOps lifecycle.

---

## Stage 1 — Git Checkout

The pipeline pulls the latest source code from GitHub repository.

```bash id="s0uxzv"
git clone <repository-url>
```

Purpose:

* Fetch latest application code
* Maintain updated deployment version

---

## Stage 2 — Install Dependencies

Required Python packages are installed automatically.

```bash id="twul0v"
pip install -r requirements.txt
```

Purpose:

* Install Flask packages
* Install MySQL connector
* Prepare application environment

---

## Stage 3 — Run Automated Tests

Application testing is executed before Docker build.

```bash id="4l0q6v"
python -m pytest
```

Purpose:

* Validate application functionality
* Detect bugs before deployment

---

## Stage 4 — Build Docker Image

The Flask application is containerized into Docker image.

```bash id="d9m8gl"
docker build -t devlog .
```

Purpose:

* Create portable application image
* Ensure consistent runtime environment

---

## Stage 5 — Docker Hub Authentication

Jenkins securely logs in to Docker Hub using stored credentials.

```bash id="evn4sd"
docker login
```

Purpose:

* Authenticate Docker registry access
* Enable image push operation

---

## Stage 6 — Tag Docker Image

Docker image is tagged before pushing.

```bash id="gw59zi"
docker tag devlog username/devlog:latest
```

Purpose:

* Create versioned image
* Prepare for Docker Hub upload

---

## Stage 7 — Push Docker Image

Docker image is pushed to Docker Hub repository.

```bash id="n4m9r5"
docker push username/devlog:latest
```

Purpose:

* Store image in centralized registry
* Enable deployment from any environment

---

## Stage 8 — Deployment

The latest Docker image is deployed.

Deployment Targets:

* AWS EC2
* Kubernetes Cluster

Purpose:

* Run latest application version
* Enable continuous deployment

---

## Stage 9 — Email Notification

Jenkins sends pipeline status notifications through email.

Notifications Include:

* Build Success
* Build Failure
* Deployment Status

Purpose:

* Continuous monitoring
* Deployment visibility

---

# 📊 Jenkins Pipeline Workflow Architecture

```text id="79mw3n"
Developer
    ↓
Push Code to GitHub
    ↓
Jenkins Master Node
    ↓
Trigger Jenkins Pipeline
    ↓
Jenkins Slave Node
    ↓
Git Checkout
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Docker Hub Login
    ↓
Push Docker Image
    ↓
Deploy Application
    ↓
Send Email Notification
```

---

# 🔄 Complete Project Workflow

```text id="x8r9al"
User
   ↓
Flask Web Application
   ↓
MySQL Database
   ↓
Docker Container
   ↓
Jenkins CI/CD Pipeline
   ↓
Docker Hub
   ↓
AWS EC2 / Kubernetes
   ↓
Terraform Infrastructure
```

---

# 🔐 Demo Credentials

| Username | Password |
| -------- | -------- |
| keerti   | demo123  |
| arjun    | demo123  |
| meera    | demo123  |

---

# 🧪 Useful Commands

## Docker Commands

```bash id="e9on7f"
docker ps
docker images
docker logs <container-id>
```

---

## Kubernetes Commands

```bash id="s07r89"
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

---

## Terraform Commands

```bash id="jlwm81"
terraform validate
terraform plan
terraform apply
```

---

# ❓ Troubleshooting

## MySQL Connection Issue

```bash id="y1wtjl"
sudo systemctl status mysql
```

---

## Docker Port Already in Use

```bash id="53zyyn"
docker ps
```

Stop conflicting container.

---

## Kubernetes Pod Logs

```bash id="lb1byr"
kubectl logs <pod-name>
```

---

## Terraform Validation

```bash id="l3th8h"
terraform validate
```

---

# 📚 Learning Outcomes

✅ Flask full-stack development
✅ MySQL database integration
✅ Authentication system
✅ Docker containerization
✅ Docker Compose orchestration
✅ Jenkins CI/CD pipeline implementation
✅ Jenkins master-slave architecture
✅ Docker Hub image management
✅ AWS EC2 deployment
✅ Kubernetes orchestration
✅ Terraform Infrastructure as Code
✅ Automated deployment workflow

---

# 👨‍💻 Author

**Keerti Patil**

---


## ⭐ GitHub

Project will be pushed to GitHub repository 
````md
# 🚀 DevLog — Team Activity Tracker
### Flask + MySQL + Docker + AWS + Kubernetes + Terraform | Internship Project

A colorful team activity tracker where developers log what they built, deployed, or learned — with kudos, timeline view, stats dashboard, leaderboard, and real-world DevOps deployment workflow.

---

## 📌 Project Highlights

✅ Built and tested locally on personal machine  
✅ Containerized using Docker  
✅ Multi-container setup using Docker Compose  
✅ Docker image pushed to Docker Hub  
✅ Hosted on AWS EC2  
✅ Deployed on Kubernetes  
✅ Infrastructure provisioned using Terraform  
✅ Ready to push on GitHub

---

## 📁 Project Structure

```bash
devlog/
├── app.py                  ← Flask backend (all routes)
├── schema.sql              ← MySQL database + sample data
├── requirements.txt        ← Python packages
├── Dockerfile              ← Docker image for Flask app
├── docker-compose.yml      ← Runs Flask + MySQL together
├── terraform/             ← Terraform IaC files
├── k8s/                   ← Kubernetes manifests
└── templates/
    ├── base.html           ← Shared layout + sidebar
    ├── login.html          ← Login page
    ├── register.html       ← Register page
    ├── dashboard.html      ← Activity feed
    ├── post.html           ← Log new activity
    ├── timeline.html       ← Timeline grouped by date
    └── stats.html          ← Leaderboard + charts
````

---

## ─────────────────────────────────────────────

## PART 1: Run on Local Machine

## ─────────────────────────────────────────────

### Step 1 — Install MySQL

**Windows:** Install MySQL Installer
**Mac:**

```bash
brew install mysql
brew services start mysql
```

**Ubuntu/Linux:**

```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

---

### Step 2 — Setup Database

```bash
mysql -u root -p
```

Run:

```sql
source schema.sql;
```

Creates:

* Database: `devlog_db`
* User: `devlog_user`
* Password: `devlog_pass`

---

### Step 3 — Create Virtual Environment

```bash
cd devlog
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

---

### Step 4 — Install Requirements

```bash
pip install -r requirements.txt
```

---

### Step 5 — Run Flask App

```bash
python app.py
```

Open:

```bash
http://localhost:5000
```

---

## ─────────────────────────────────────────────

## PART 2: Run with Docker

## ─────────────────────────────────────────────

### Build Image

```bash
docker build -t devlog .
```

### Run Container

```bash
docker run -d -p 5000:5000 devlog
```

Open:

```bash
http://localhost:5000
```

---

## ─────────────────────────────────────────────

## PART 3: Run with Docker Compose

## ─────────────────────────────────────────────

Runs Flask + MySQL together.

```bash
docker compose up --build -d
```

Useful commands:

```bash
docker compose logs
docker compose down
docker compose down -v
docker ps
```

---

## ─────────────────────────────────────────────

## PART 4: Push Image to Docker Hub

## ─────────────────────────────────────────────

```bash
docker login
docker tag devlog yourdockerhubusername/devlog:latest
docker push yourdockerhubusername/devlog:latest
```

---

## ─────────────────────────────────────────────

## PART 5: Deploy on AWS EC2

## ─────────────────────────────────────────────

### Launch EC2 Instance

Open ports:

* 22 (SSH)
* 80
* 5000

### Connect Server

```bash
ssh -i key.pem ubuntu@your-public-ip
```

### Install Docker & Run App

```bash
docker pull yourdockerhubusername/devlog:latest
docker run -d -p 80:5000 yourdockerhubusername/devlog:latest
```

Access:

```bash
http://your-public-ip
```

---

## ─────────────────────────────────────────────

## PART 6: Deploy on Kubernetes

## ─────────────────────────────────────────────

Inside `k8s/` folder:

```bash
kubectl apply -f .
```

Verify:

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
```

---

## ─────────────────────────────────────────────

## PART 7: Terraform Infrastructure

## ─────────────────────────────────────────────

Inside `terraform/` folder:

```bash
terraform init
terraform plan
terraform apply
```

Destroy:

```bash
terraform destroy
```

---

## 🔧 How Architecture Works

```text
Browser
   ↓
Flask App
   ↓
MySQL Database
   ↓
Docker Container
   ↓
AWS EC2 / Kubernetes
   ↓
Provisioned using Terraform
```

---

## 🌟 Features Summary

| Feature       | Route       | Description           |
| ------------- | ----------- | --------------------- |
| Login         | /login      | Secure authentication |
| Register      | /register   | New user signup       |
| Dashboard     | /dashboard  | Activity feed         |
| Post Activity | /post       | Add new work logs     |
| Timeline      | /timeline   | Activities by date    |
| Stats         | /stats      | Charts + leaderboard  |
| Kudos         | /kudos/<id> | Like system           |

---

## 🎨 Tech Stack

* Python 3.11
* Flask
* MySQL
* HTML / CSS / JS
* Docker
* Docker Compose
* Docker Hub
* AWS EC2
* Kubernetes
* Terraform

---

## 🔐 Demo Login

| Username | Password |
| -------- | -------- |
| keerti   | demo123  |
| arjun    | demo123  |
| meera    | demo123  |

---

## ❓ Troubleshooting

### MySQL not connecting

```bash
sudo systemctl status mysql
```

### Docker port already used

```bash
docker ps
```

Stop conflicting container.

### Kubernetes pod issue

```bash
kubectl logs <pod-name>
```

### Terraform issue

```bash
terraform validate
```

---

## 📚 Learning Outcomes

✅ Flask full-stack development
✅ Database integration
✅ Authentication system
✅ Docker containerization
✅ Docker Compose orchestration
✅ Docker Hub image management
✅ AWS hosting
✅ Kubernetes deployment
✅ Terraform Infrastructure as Code

---

## 👨‍💻 Author

**Keerti patil

## ⭐ GitHub

Project will be pushed to GitHub repository 
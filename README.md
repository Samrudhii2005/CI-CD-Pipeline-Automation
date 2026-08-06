# 🚀 CI/CD Pipeline Automation for FastAPI Cloud Applications

An empirical implementation of a **CI/CD pipeline** for a FastAPI-based cloud application using **GitHub Actions**, **SonarQube**, and **Render**. This project demonstrates automated testing, code quality analysis, deployment validation, secure secret management, and deployment automation following modern DevOps practices.

## ✨ Features

- ⚡ FastAPI REST API
- 🔄 Automated CI/CD with GitHub Actions
- 🧪 Automated Unit Testing using Pytest
- 📊 Code Coverage Reporting
- 🔍 SonarQube Code Quality Analysis
- ✅ Quality Gate Validation
- ❤️ Automated Health Check
- 🔐 GitHub Secrets Integration
- 🚀 Render Cloud Deployment
- 🔄 Deployment Gating using Render Deploy Hook
- ♻️ Simulated Automated Rollback

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- MySQL
- SQLAlchemy
- GitHub Actions
- SonarQube Cloud
- Pytest
- Render

## 📊 Experimental Evaluation

The pipeline was evaluated using controlled fault injection experiments including:

- Unit Test Failure Detection
- Syntax Error Detection
- Health Check Validation
- Health Check Failure Detection
- Environment Variable Failure
- Rollback Simulation
- SonarQube Quality Analysis
- Pipeline Reliability Evaluation

## 📈 Key Results

| Metric | Result |
|---------|--------|
| Quality Gate | ✅ Passed |
| Code Coverage | **65.2%** |
| Code Duplication | **0.0%** |
| Open Issues | **21** |
| Pipeline Reliability* | **100%** |

> *Reliability measured across the conducted experimental scenarios.*

## 🚀 Getting Started

```bash
git clone https://github.com/Samrudhii2005/CI-CD-Pipeline-Automation.git
cd CI-CD-Pipeline-Automation

python -m venv venv

# Activate Virtual Environment
venv\Scripts\activate

pip install -r requirements.txt

python create_tables.py

uvicorn app.main:app --reload
```

## 🧪 Run Tests

```bash
pytest
```

Generate coverage report:

```bash
pytest --cov=. --cov-report=xml
```

## 📌 Future Enhancements

- Docker Containerization
- Kubernetes Deployment
- Terraform Integration
- Prometheus & Grafana Monitoring
- Blue-Green Deployment
- Canary Deployment

## 👨‍💻 Author

**Samrudhi Ghanate**

B.Tech Computer Science Engineering (Cloud Computing)

Research Internship Project

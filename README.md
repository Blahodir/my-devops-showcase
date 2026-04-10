# 🚀 DevOps Showcase: Automated CI/CD Pipeline with AWS & Docker

This project demonstrates a production-ready CI/CD workflow, bridging the gap between local development and cloud infrastructure. 
It features a containerized Python application deployed on AWS EC2, with automated security scanning and image management.

## 🛠 Tech Stack
* **Cloud:** AWS EC2 (t3.micro)
* **Containerization:** Docker & Docker Hub
* **CI/CD:** GitHub Actions
* **Security:** Trivy Vulnerability Scanner
* **Environment:** Linux (Ubuntu)

## 🏗 System Architecture
The pipeline follows a modern DevOps lifecycle:
1.  **Version Control:** Code is pushed to GitHub.
2.  **Continuous Integration:** GitHub Actions triggers a build process.
3.  **Security Gate:** **Trivy** scans the Docker image for OS and library vulnerabilities.
4.  **Artifact Management:** Upon passing the scan, the image is pushed to **Docker Hub** using secure Access Tokens.
5.  **Continuous Deployment:** The application is deployed to an **AWS EC2** instance, utilizing Docker for environment consistency.



## 🚀 Deployment Instructions

### Local Quickstart
To run the application locally (port 8000):
docker pull madlizard/app:latest
docker run -p 8000:8000 madlizard/app:latest

## Manual Cloud Deployment (AWS)
ssh -i "your-key.pem" ubuntu@your-aws-ip
docker login -u madlizard
docker run -d -p 80:8000 --name my-app madlizard/app:latest

## 🔒 Security Hardening
Infrastructure: Configured AWS Security Groups to restrict inbound traffic to essential ports only (22 for SSH, 80 for HTTP).
Secrets Management: Sensitive data like SSH keys and Docker tokens are managed via GitHub Secrets.
Minimal Permissions: Implemented a non-root execution policy within the container environment.

Developed by: madlizard

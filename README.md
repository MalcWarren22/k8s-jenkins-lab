# Kubernetes + Jenkins CI/CD Pipeline 

A **production-style CI/CD pipeline** that builds, deploys, and safely rolls out an application to Kubernetes using **Jenkins, Docker, and k3d (k3s)** — all running locally on **WSL2**.

This lab was intentionally designed to go **beyond “it works”** and instead focus on **real DevOps engineering practices**: secure configuration, rollout safety, failure handling, and operational debugging.

---

## Technologies Used

- **Jenkins** – CI/CD orchestration (running in Docker)
- **Docker** – Image build, tagging, and runtime
- **Kubernetes (k3s via k3d)** – Container orchestration
- **kubectl** – Cluster management and rollout control
- **WSL2 (Ubuntu)** – Local Linux development environment

---

## Project Objectives

The goal of this project was to **design and implement** a realistic CI/CD workflow that mirrors production environments.

Key objectives included:
- Running Jenkins in a containerized environment
- Deploying applications to Kubernetes via CI
- Securely handling Kubernetes credentials
- Enabling zero-downtime deployments
- Debugging real-world DevOps issues across layers

---

## What This Project Demonstrates

This project highlights **hands-on DevOps engineering skills**, including:

- End-to-end CI/CD pipeline design with Jenkins
- Jenkins → Kubernetes integration (no shortcuts or manual steps)
- Secure kubeconfig generation and handling inside CI
- Docker image build, tagging, and promotion strategy
- **Zero-downtime rolling deployments**
- Kubernetes **readiness, liveness, and startup probes**
- **Pod Disruption Budgets (PDBs)** to enforce availability guarantees
- Troubleshooting:
  - Container networking issues
  - Kubernetes API authentication & permissions
  - CI environment pathing and tooling conflicts

This reflects **real production challenges and fixes**, not a “happy-path” demo.

---

## 🏗️ CI/CD Pipeline Flow

1. **Source Checkout**
   - Jenkins pulls the latest code from GitHub

2. **Build & Tag**
   - Docker image is built from the application source
   - Image is tagged using the Jenkins build number

3. **Image Injection**
   - Image is imported directly into the local k3d cluster

4. **Deploy to Kubernetes**
   - Kubernetes manifests are applied via `kubectl`
   - Rolling update strategy ensures no downtime

5. **Verification**
   - Kubernetes health probes validate pod readiness
   - Rollout status is monitored for failures

---

## Repository Structure

```text
k8s-jenkins-lab/
├── app/                         # Flask application source + Dockerfile
├── k8s/                         # Kubernetes manifests
│   ├── deployment.yaml          # Rolling deployment with health probes
│   ├── service.yaml             # NodePort service exposure
│   └── pdb.yaml                 # Pod Disruption Budget
├── jenkins/                     # Jenkins infrastructure
│   ├── Dockerfile               # Custom Jenkins image (Docker, kubectl, k3d)
│   └── kubeconfig.template.yaml # Kubeconfig template/reference
├── Jenkinsfile                  # CI/CD pipeline definition
├── .gitignore
└── README.md

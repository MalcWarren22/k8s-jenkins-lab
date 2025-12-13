\# Kubernetes + Jenkins CI/CD Pipeline (Local DevOps Lab)



This project demonstrates a \*\*production-style CI/CD pipeline\*\* that builds, deploys, and safely rolls out an application to Kubernetes using \*\*Jenkins, Docker, and k3d (k3s)\*\* — all running locally via \*\*WSL2\*\*.



The goal of this lab was not just to “make it work,” but to \*\*design, debug, and harden\*\* a real DevOps workflow end to end.



---



\## Technologies Used



\- \*\*Jenkins\*\* – CI/CD orchestration (running in Docker)

\- \*\*Docker\*\* – Image build, tagging, and runtime

\- \*\*Kubernetes (k3s via k3d)\*\* – Container orchestration

\- \*\*kubectl\*\* – Cluster control and rollout management

\- \*\*WSL2 (Ubuntu)\*\* – Local Linux environment



---



\## What This Project Demonstrates



This project showcases \*\*real DevOps engineering skills\*\*, including:



\- End-to-end CI/CD pipeline design

\- Jenkins → Kubernetes integration without shortcuts

\- Secure kubeconfig generation and handling inside CI

\- Zero-downtime \*\*rolling deployments\*\*

\- Kubernetes \*\*readiness, liveness, and startup probes\*\*

\- Pod Disruption Budgets (PDBs) for availability guarantees

\- Debugging container networking, permissions, and API access issues



This mirrors \*\*real production problems and fixes\*\*, not a “happy path” demo.



---



\## Repository Structure



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


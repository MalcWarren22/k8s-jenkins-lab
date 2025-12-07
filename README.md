# Kubernetes + Jenkins CI/CD Lab

This project demonstrates a complete local CI/CD pipeline using:

- Docker
- Kubernetes (k3d / k3s)
- Jenkins
- WSL2 (Ubuntu)

## Architecture

- Flask application containerized with Docker
- Local Kubernetes cluster via k3d
- Jenkins runs in Docker and deploys to the cluster using kubectl

## Project Structure

- app/ # Flask app + Dockerfile
- k8s/ # Kubernetes manifests
- Jenkinsfile # CI/CD pipeline

## How it works

1. Jenkins builds the Docker image
2. Jenkins imports the image into k3d
3. Jenkins deploys the app to Kubernetes
4. App is exposed locally via port-forward

## Status
- Local CI/CD pipeline working
- Jenkins -> Kubernetes integration complete


FROM jenkins/jenkins:lts

USER root

# Install dependencies + docker cli
RUN apt-get update && \
    apt-get install -y curl ca-certificates docker.io && \
    rm -rf /var/lib/apt/lists/*

# Install kubectl (server version v1.31.5)
RUN curl -fsSL -o /usr/local/bin/kubectl \
    https://dl.k8s.io/release/v1.31.5/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl

# Install k3d
RUN curl -fsSL https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash

USER jenkins

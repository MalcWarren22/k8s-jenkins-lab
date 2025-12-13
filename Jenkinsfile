pipeline {
  agent any

  environment {
    APP_NAME   = "devops-lab-app"
    IMAGE_TAG  = "${env.BUILD_NUMBER}"
    CLUSTER    = "dev-cluster"

    KUBECONFIG = "/var/jenkins_home/.kube/config"

    DEPLOYMENT = "devops-lab-app"
    CONTAINER  = "devops-lab-app"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker image') {
      steps {
        dir('app') {
          sh '''
            docker build -t ${APP_NAME}:${IMAGE_TAG} .
            docker tag ${APP_NAME}:${IMAGE_TAG} ${APP_NAME}:latest
          '''
        }
      }
    }

    stage('Import image into k3d') {
      steps {
        sh '''
          k3d image import ${APP_NAME}:${IMAGE_TAG} -c ${CLUSTER}
          k3d image import ${APP_NAME}:latest -c ${CLUSTER}
        '''
      }
    }

    stage('Configure kubeconfig (k3d DNS fix)') {
      steps {
        sh '''
          set -e
          mkdir -p "$(dirname "${KUBECONFIG}")"

          # Create/refresh kubeconfig from k3d (required)
          k3d kubeconfig get "${CLUSTER}" > "${KUBECONFIG}"

          # Permanent fix: rewrite server line regardless of indentation / previous value
          sed -i 's#^[[:space:]]*server:.*#    server: https://k3d-dev-cluster-server-0:6443#g' "${KUBECONFIG}"

          # Proof / sanity (force kubectl to use this exact kubeconfig)
          KUBECONFIG="${KUBECONFIG}" kubectl cluster-info
          KUBECONFIG="${KUBECONFIG}" kubectl auth can-i get pods
        '''
      }
    }

    stage('Deploy to Kubernetes (apply)') {
      steps {
        sh '''
          # Always force kubectl to use the intended kubeconfig (each sh block is a new shell)
          KUBECONFIG="${KUBECONFIG}" kubectl cluster-info

          # PERMA FIX: disable OpenAPI validation (your environment fails OpenAPI fetch)
          KUBECONFIG="${KUBECONFIG}" kubectl apply --validate=false -f k8s/

          KUBECONFIG="${KUBECONFIG}" kubectl get deploy "${DEPLOYMENT}"
        '''
      }
    }

    stage('Rollout (zero-downtime) + Gate') {
      steps {
        sh '''
          # Image Rollout
          KUBECONFIG="${KUBECONFIG}" kubectl set image deployment/"${DEPLOYMENT}" "${CONTAINER}"="${APP_NAME}:${IMAGE_TAG}"

          # Fail the pipeline if rollout doesn't complete
          KUBECONFIG="${KUBECONFIG}" kubectl rollout status deployment/"${DEPLOYMENT}" --timeout=180s

          # Log Proof
          KUBECONFIG="${KUBECONFIG}" kubectl rollout history deployment/"${DEPLOYMENT}"
        '''
      }
    }
  }

  post {
    always {
      sh '''
        KUBECONFIG="/var/jenkins_home/.kube/config" kubectl get pods -l app="${DEPLOYMENT}" -o wide || true
        KUBECONFIG="/var/jenkins_home/.kube/config" kubectl describe deployment/"${DEPLOYMENT}" || true
      '''
    }
  }
}


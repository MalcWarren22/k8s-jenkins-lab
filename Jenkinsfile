pipeline {
    agent any

    environment {
        APP_NAME   = "devops-lab-app"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
        KUBECONFIG = "/var/jenkins_home/.kube/config"
        CLUSTER    = "dev-cluster"
    }

    stages {
        stage('Checkout') {
            steps {
                // Uses the repo configured in the job
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                dir('app') {
                    sh 'docker build -t ${APP_NAME}:${IMAGE_TAG} .'
                    sh 'docker tag ${APP_NAME}:${IMAGE_TAG} ${APP_NAME}:latest'
                }
            }
        }

        stage('Import image into k3d') {
            steps {
                sh 'k3d image import ${APP_NAME}:${IMAGE_TAG} -c ${CLUSTER}'
                sh 'k3d image import ${APP_NAME}:latest -c ${CLUSTER}'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl get pods'
            }
        }
    }
}

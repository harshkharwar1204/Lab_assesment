pipeline {
    agent any

    tools {
        // This name must exactly match the one you just saved
        docker 'docker-tool'
    }
    
    environment {
        // Replace 'your-dockerhub-username' with your actual username
        DOCKER_IMAGE = "kharwarharsh1204/flask-app:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE, '.')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // This uses the credential ID you set up in Jenkins
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }
    }
}
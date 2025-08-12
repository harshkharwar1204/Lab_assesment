pipeline {
    // This line tells Jenkins to run all steps inside the official 'docker' container
    agent {
        docker { image 'docker:latest' }
    }

    environment {
        // Your Docker Hub username and image name
        DOCKER_IMAGE = "kharwarharsh1204/flask-app:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build and Push Image') {
            steps {
                script {
                    // Use the credentials you stored in Jenkins
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        
                        // Build the image
                        def customImage = docker.build(DOCKER_IMAGE, '.')

                        // Push the image to your Docker Hub repository
                        customImage.push()
                    }
                }
            }
        }
    }
}
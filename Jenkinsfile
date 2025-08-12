pipeline {
    agent {
        docker { image 'docker:latest' }
    }

    environment {
        // Docker Hub configuration
        DOCKER_REGISTRY = 'registry.hub.docker.com'
        DOCKER_IMAGE_NAME = 'dhruv99269/flask-app'
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
        DOCKER_IMAGE_LATEST = "${DOCKER_IMAGE_NAME}:latest"
        
        // Credentials ID (make sure this exists in Jenkins)
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Starting build for ${env.BUILD_NUMBER}"
                    echo "Building Docker image: ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo "Building Docker image..."
                        sh "docker build -t ${DOCKER_IMAGE} -t ${DOCKER_IMAGE_LATEST} ."
                        echo "Docker image built successfully"
                    } catch (Exception e) {
                        echo "Failed to build Docker image: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        error "Docker build failed"
                    }
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    try {
                        echo "Testing Docker image..."
                        // Run a quick test to ensure the image works
                        sh "docker run --rm ${DOCKER_IMAGE} python -c 'import flask; print(\"Flask imported successfully\")'"
                        echo "Docker image test passed"
                    } catch (Exception e) {
                        echo "Failed to test Docker image: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        error "Docker test failed"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    try {
                        echo "Logging into Docker Hub..."
                        withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                            sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                        }
                        
                        echo "Pushing image to Docker Hub..."
                        sh "docker push ${DOCKER_IMAGE}"
                        sh "docker push ${DOCKER_IMAGE_LATEST}"
                        
                        echo "Successfully pushed ${DOCKER_IMAGE} and ${DOCKER_IMAGE_LATEST} to Docker Hub"
                    } catch (Exception e) {
                        echo "Failed to push to Docker Hub: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        error "Docker Hub push failed"
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    try {
                        echo "Cleaning up local Docker images..."
                        sh "docker rmi ${DOCKER_IMAGE} ${DOCKER_IMAGE_LATEST} || true"
                        echo "Cleanup completed"
                    } catch (Exception e) {
                        echo "Cleanup failed (non-critical): ${e.getMessage()}"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Build ${env.BUILD_NUMBER} completed with result: ${currentBuild.result}"
            }
        }
        success {
            script {
                echo "✅ Build successful! Docker image ${DOCKER_IMAGE} has been built and pushed to Docker Hub"
                echo "📦 Image available at: https://hub.docker.com/r/${DOCKER_IMAGE_NAME}"
            }
        }
        failure {
            script {
                echo "❌ Build failed! Check the logs above for details"
            }
        }
    }
}
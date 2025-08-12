# Jenkins Setup Guide

This guide will help you configure Jenkins to build and push Docker images to Docker Hub.

## Prerequisites

1. Jenkins server with Docker plugin installed
2. Docker Hub account
3. Access to Jenkins admin panel

## Step 1: Install Required Jenkins Plugins

Make sure the following plugins are installed in Jenkins:
- Docker Pipeline
- Credentials Binding
- Pipeline Utility Steps

## Step 2: Configure Docker Hub Credentials

1. Go to **Jenkins Dashboard** → **Manage Jenkins** → **Manage Credentials**
2. Click on **System** → **Global credentials** → **Add Credentials**
3. Configure the credentials:
   - **Kind**: Username with password
   - **Scope**: Global
   - **Username**: Your Docker Hub username
   - **Password**: Your Docker Hub password or access token
   - **ID**: `dockerhub-credentials`
   - **Description**: Docker Hub credentials for pushing images

## Step 3: Configure Jenkins Agent

Ensure your Jenkins agent has:
- Docker daemon running
- Docker CLI installed
- Proper permissions to run Docker commands

## Step 4: Create Jenkins Pipeline

1. Go to **Jenkins Dashboard** → **New Item**
2. Select **Pipeline** and give it a name
3. In the pipeline configuration:
   - **Definition**: Pipeline script from SCM
   - **SCM**: Git
   - **Repository URL**: Your Git repository URL
   - **Branch**: Your main branch (e.g., `main` or `master`)
   - **Script Path**: `Jenkinsfile`

## Step 5: Run the Pipeline

1. Click **Build Now** to start the pipeline
2. Monitor the build logs for any issues
3. The pipeline will:
   - Build the Docker image
   - Test the image
   - Push to Docker Hub with tags: `latest` and build number
   - Clean up local images

## Troubleshooting

### Common Issues:

1. **Docker permission denied**:
   ```bash
   # Add jenkins user to docker group
   sudo usermod -aG docker jenkins
   sudo systemctl restart jenkins
   ```

2. **Docker Hub authentication failed**:
   - Verify credentials are correct
   - Use Docker Hub access token instead of password
   - Check if 2FA is enabled (use access token)

3. **Build fails with missing dependencies**:
   - Ensure all required files are in the repository
   - Check if `.dockerignore` is not excluding necessary files

4. **Port already in use**:
   - The Dockerfile exposes port 5000
   - Ensure this port is available or modify the Dockerfile

## Docker Hub Repository

After successful builds, your images will be available at:
- `https://hub.docker.com/r/kharwarharsh1204/flask-app`

## Image Tags

The pipeline creates two tags:
- `kharwarharsh1204/flask-app:latest` - Latest version
- `kharwarharsh1204/flask-app:{BUILD_NUMBER}` - Versioned by build number

## Security Notes

- The Dockerfile runs as a non-root user for security
- Credentials are stored securely in Jenkins
- Images are cleaned up after pushing to save disk space

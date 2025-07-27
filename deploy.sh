#!/bin/bash

# Docker Hub Deployment Script
# Replace 'your-username' with your actual Docker Hub username

DOCKER_USERNAME="helhamaky"
IMAGE_NAME="twerlo-RAG"
VERSION="1.0.0"

echo "🚀 Deploying Twerlo RAG System to Docker Hub..."

# Tag the image
echo "📝 Tagging image..."
docker tag ${IMAGE_NAME}:latest ${DOCKER_USERNAME}/${IMAGE_NAME}:latest
docker tag ${IMAGE_NAME}:latest ${DOCKER_USERNAME}/${IMAGE_NAME}:v${VERSION}

# Login to Docker Hub
echo "🔐 Logging in to Docker Hub..."
docker login

# Push images
echo "⬆️ Pushing images to Docker Hub..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:latest
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:v${VERSION}

echo "✅ Deployment complete!"
echo "📦 Image available at: ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
echo "📦 Versioned image: ${DOCKER_USERNAME}/${IMAGE_NAME}:v${VERSION}" 
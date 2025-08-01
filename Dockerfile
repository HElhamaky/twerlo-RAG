# Multi-stage build for production
FROM node:18-alpine AS frontend-builder

# Set working directory
WORKDIR /app/frontend

# Copy package files first for better caching
COPY frontend/package*.json ./

# Install all dependencies (including dev dependencies) for building
RUN npm ci --verbose

# Copy frontend source code
COPY frontend/ ./

# Ensure public directory exists
RUN mkdir -p public

# Build the frontend application
RUN npm run build

# Verify build output
RUN ls -la
RUN ls -la public/ || echo "Public directory not found"

# Production stage
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy built frontend from builder stage
COPY --from=frontend-builder /app/frontend/.next ./frontend/.next
COPY --from=frontend-builder /app/frontend/public ./frontend/public
COPY --from=frontend-builder /app/frontend/package*.json ./frontend/

# Install frontend dependencies for production
WORKDIR /app/frontend
RUN npm ci --only=production

# Create data directory
WORKDIR /app
RUN mkdir -p data/chroma_db && chmod 755 data

# Copy startup script and ensure proper line endings
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh && \
    sed -i 's/\r$//' /app/start.sh

# Set environment variables
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
ENV PORT=3000

# Expose ports
EXPOSE 3000 8000

# Start the application
CMD ["/bin/bash", "/app/start.sh"] 
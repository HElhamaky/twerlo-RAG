#!/bin/bash
set -e

echo "Starting Twerlo application..."

# Initialize database
echo "Initializing database..."
cd /app
python -m app.db.init_db

# Start the backend API server
echo "Starting backend..."
cd /app
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# Wait a moment for backend to start
sleep 5

# Test backend health
echo "Testing backend health..."
curl -f http://localhost:8000/health || echo "Backend health check failed"

# Start the frontend server
echo "Starting frontend..."
cd /app/frontend
npm start &

# Wait for both processes
wait 
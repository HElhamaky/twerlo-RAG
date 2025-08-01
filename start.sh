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

# Wait for backend to be ready
echo "Waiting for backend to be ready..."
for i in {1..30}; do
  if curl -f http://127.0.0.1:8000/health > /dev/null 2>&1; then
    echo "Backend is ready!"
    break
  fi
  echo "Waiting for backend... attempt $i/30"
  sleep 2
done

# Final health check
echo "Final backend health check..."
curl -f http://127.0.0.1:8000/health || echo "Backend health check failed"

# Start the frontend server
echo "Starting frontend..."
cd /app/frontend
npm start &

# Wait for both processes
wait 
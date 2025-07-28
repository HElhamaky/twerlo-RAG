#!/bin/bash

echo "Starting Twerlo application..."

# Start the backend API server
echo "Starting backend..."
cd /app
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start the frontend server
echo "Starting frontend..."
cd /app/frontend
npm start &

# Wait for both processes
wait 
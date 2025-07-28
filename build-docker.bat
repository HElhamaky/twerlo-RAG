@echo off
echo Building and running Twerlo with Docker...
echo.

echo Stopping any existing containers...
docker-compose down

echo.
echo Building Docker image...
docker-compose build --no-cache

echo.
echo Starting services...
docker-compose up -d

echo.
echo Services are starting up...
echo Frontend will be available at: http://localhost:3000
echo Backend API will be available at: http://localhost:8000
echo.
echo To view logs: docker-compose logs -f
echo To stop services: docker-compose down
echo.
pause 
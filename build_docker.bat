@echo off
echo Building FastAPI RAG System Docker image...
docker build -t rag-app .

if %ERRORLEVEL% EQU 0 (
    echo Build successful!
    echo.
    echo To run the container, use:
    echo docker run -p 8000:8000 -v %cd%/data:/app/data --env-file .env rag-app
    echo.
    echo Or use docker-compose:
    echo docker-compose up
) else (
    echo Build failed! Please check the error messages above.
) 
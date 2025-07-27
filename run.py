#!/usr/bin/env python3
"""
FastAPI RAG System Startup Script
"""

import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "true").lower() == "true"
    
    print(f"Starting FastAPI RAG System on {host}:{port}")
    print("API Documentation will be available at:")
    print(f"  - http://{host}:{port}/docs")
    print(f"  - http://{host}:{port}/redoc")
    
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    ) 
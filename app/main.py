from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, documents, qa
from app.db.database import engine
from app.db.models import Base
import os

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="FastAPI RAG System",
    description="A Retrieval-Augmented Generation system with document upload and question answering",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(qa.router)

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "FastAPI RAG System",
        "version": "1.0.0",
        "endpoints": {
            "auth": {
                "register": "POST /auth/register",
                "login": "POST /auth/login"
            },
            "documents": {
                "upload": "POST /documents/upload"
            },
            "qa": {
                "ask": "POST /qa/ask"
            }
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"} 
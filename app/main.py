from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, documents, qa
from app.db.database import engine
from app.db.models import Base
from app.db.init_db import init_database
import os

# Initialize database
init_database()

app = FastAPI(title="Twerlo API", version="1.0.0")

# Get CORS origins from environment or use defaults
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")
cors_origins.append("*")  # Allow all origins for development

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(qa.router, prefix="/qa", tags=["qa"])

@app.get("/")
async def root():
    return {"message": "Twerlo API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Twerlo API is operational"}

@app.get("/cors-test")
async def cors_test():
    return {"message": "CORS is working correctly"} 
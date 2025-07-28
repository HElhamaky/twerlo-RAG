from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # Security
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Database Configuration
    chroma_db_path: str = os.getenv("CHROMA_DB_PATH", "data/chroma_db")
    database_url: str = "sqlite:///./rag_app.db"
    
    # LLM Configuration - Using optimized models
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")  # Cost-effective GPT-4 model
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")  # High-quality embedding model
    
    # Application Configuration
    chunk_size: int = 500
    chunk_overlap: int = 50
    similarity_search_k: int = 3
    
    class Config:
        env_file = ".env"

settings = Settings() 
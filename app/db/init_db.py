from sqlalchemy import create_engine
from app.db.models import Base
from app.core.config import settings
import os

def init_database():
    """Initialize the database and create tables."""
    # Ensure data directory exists
    data_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Create database engine
    engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    print(f"Database initialized at: {settings.database_url}")

if __name__ == "__main__":
    init_database() 
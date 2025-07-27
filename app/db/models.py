from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Relationship to QueryLog
    query_logs = relationship("QueryLog", back_populates="user")

class QueryLog(Base):
    __tablename__ = "query_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    time_to_respond = Column(Float, nullable=False)  # Response time in seconds
    question = Column(Text, nullable=False)
    llm_response = Column(Text, nullable=False)
    
    # Relationship to User
    user = relationship("User", back_populates="query_logs") 
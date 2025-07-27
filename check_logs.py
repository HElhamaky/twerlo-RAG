#!/usr/bin/env python3
"""
Script to check and display logs from the FastAPI RAG system
"""

from app.db.database import SessionLocal
from app.db.models import QueryLog, User
from datetime import datetime

def check_logs():
    """Display all query logs from the database"""
    db = SessionLocal()
    try:
        # Get all query logs
        logs = db.query(QueryLog).order_by(QueryLog.timestamp.desc()).all()
        
        print(f"=== FastAPI RAG System - Query Logs ===")
        print(f"Total queries logged: {len(logs)}")
        print(f"Database: {db.bind.url}")
        print("=" * 50)
        
        if not logs:
            print("No query logs found.")
            return
        
        # Display recent logs
        for i, log in enumerate(logs[:10]):  # Show last 10 logs
            print(f"\n{i+1}. Query Log #{log.id}")
            print(f"   User ID: {log.user_id}")
            print(f"   Timestamp: {log.timestamp}")
            print(f"   Response Time: {log.time_to_respond:.2f} seconds")
            print(f"   Question: {log.question[:100]}{'...' if len(log.question) > 100 else ''}")
            print(f"   Response: {log.llm_response[:100]}{'...' if len(log.llm_response) > 100 else ''}")
            print("-" * 30)
        
        if len(logs) > 10:
            print(f"\n... and {len(logs) - 10} more logs")
            
    except Exception as e:
        print(f"Error reading logs: {e}")
    finally:
        db.close()

def check_users():
    """Display all registered users"""
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"\n=== Registered Users ===")
        print(f"Total users: {len(users)}")
        for user in users:
            print(f"User ID: {user.id}, Email: {user.email}")
    except Exception as e:
        print(f"Error reading users: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()
    check_logs() 
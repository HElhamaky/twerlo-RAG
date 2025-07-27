#!/usr/bin/env python3
"""
Detailed log analysis for the FastAPI RAG system
"""

from app.db.database import SessionLocal
from app.db.models import QueryLog, User
from datetime import datetime, timedelta
import statistics

def analyze_logs():
    """Analyze logs with detailed statistics"""
    db = SessionLocal()
    try:
        logs = db.query(QueryLog).all()
        users = db.query(User).all()
        
        print("=== FastAPI RAG System - Log Analysis ===")
        print(f"Total Users: {len(users)}")
        print(f"Total Queries: {len(logs)}")
        print("=" * 50)
        
        if not logs:
            print("No queries to analyze.")
            return
        
        # Response time statistics
        response_times = [log.time_to_respond for log in logs]
        avg_time = statistics.mean(response_times)
        min_time = min(response_times)
        max_time = max(response_times)
        
        print(f"\n📊 Performance Statistics:")
        print(f"   Average Response Time: {avg_time:.2f} seconds")
        print(f"   Fastest Response: {min_time:.2f} seconds")
        print(f"   Slowest Response: {max_time:.2f} seconds")
        
        # User activity
        user_activity = {}
        for log in logs:
            user_activity[log.user_id] = user_activity.get(log.user_id, 0) + 1
        
        print(f"\n👥 User Activity:")
        for user_id, count in user_activity.items():
            user_email = next((u.email for u in users if u.id == user_id), "Unknown")
            print(f"   User {user_id} ({user_email}): {count} queries")
        
        # Recent activity
        now = datetime.utcnow()
        recent_logs = [log for log in logs if (now - log.timestamp) < timedelta(hours=24)]
        
        print(f"\n🕒 Recent Activity (Last 24h):")
        print(f"   Queries in last 24h: {len(recent_logs)}")
        
        # Most common question patterns
        questions = [log.question.lower() for log in logs]
        common_words = {}
        for question in questions:
            words = question.split()
            for word in words:
                if len(word) > 3:  # Skip short words
                    common_words[word] = common_words.get(word, 0) + 1
        
        if common_words:
            top_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"\n🔍 Common Question Patterns:")
            for word, count in top_words:
                print(f"   '{word}': {count} times")
        
    except Exception as e:
        print(f"Error analyzing logs: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    analyze_logs() 
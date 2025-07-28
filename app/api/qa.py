from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
import time
from datetime import datetime
from app.db.database import get_db
from app.db.models import User, QueryLog
from app.core.security import get_current_user
from app.core.llm_utils import generate_embeddings, get_llm_response
from app.services.vector_store import vector_store
from app.core.config import settings

router = APIRouter(tags=["question-answering"])

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=QuestionResponse)
async def ask_question(
    question_data: QuestionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Ask a question and get an answer based on uploaded documents."""
    
    start_time = time.time()
    
    try:
        # Generate embedding for the question
        question_embedding = generate_embeddings(question_data.question)
        
        # Search for similar documents
        similar_docs = vector_store.similarity_search(
            query_embedding=question_embedding,
            k=settings.similarity_search_k,
            user_id=current_user.id
        )
        
        # Prepare context from retrieved documents
        if similar_docs:
            context = "\n\n".join(similar_docs)
        else:
            context = "No relevant documents found."
        
        # Get LLM response
        llm_response = get_llm_response(question_data.question, context)
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the query
        query_log = QueryLog(
            user_id=current_user.id,
            time_to_respond=response_time,
            question=question_data.question,
            llm_response=llm_response
        )
        
        try:
            db.add(query_log)
            db.commit()
        except Exception as e:
            # Log error but don't fail the request
            print(f"Error logging query: {str(e)}")
            db.rollback()
        
        return QuestionResponse(answer=llm_response)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question: {str(e)}"
        ) 
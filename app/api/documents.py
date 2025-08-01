from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from pydantic import BaseModel
import PyPDF2
import io
import uuid
import os
from typing import List
from datetime import datetime
from app.db.database import get_db
from app.db.models import User, Document
from app.core.security import get_current_user
from app.core.llm_utils import generate_embeddings, split_text_into_chunks
from app.services.vector_store import vector_store

router = APIRouter(tags=["documents"])

class UploadResponse(BaseModel):
    message: str
    chunks_processed: int

class DocumentInfo(BaseModel):
    id: int
    filename: str
    size: int
    uploaded_at: datetime
    chunks_count: int

@router.get("/", response_model=List[DocumentInfo])
async def list_documents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all documents for the current user."""
    try:
        # Query actual documents from database
        documents = db.query(Document).filter(Document.user_id == current_user.id).all()
        
        return [
            DocumentInfo(
                id=doc.id,
                filename=doc.original_filename,
                size=doc.file_size,
                uploaded_at=doc.uploaded_at,
                chunks_count=doc.chunks_count
            )
            for doc in documents
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error listing documents: {str(e)}"
        )

@router.post("/upload", response_model=UploadResponse)
async def upload_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload and process a document (PDF or TXT)."""
    
    # Validate file type
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file provided"
        )
    
    allowed_extensions = ['.pdf', '.txt']
    file_extension = file.filename.lower().split('.')[-1]
    
    if f'.{file_extension}' not in allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not supported. Allowed types: {', '.join(allowed_extensions)}"
        )
    
    try:
        # Read file content
        content = await file.read()
        file_size = len(content)
        
        # Parse content based on file type
        if file_extension == 'pdf':
            text_content = extract_pdf_text(content)
        else:  # txt
            text_content = content.decode('utf-8')
        
        if not text_content.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File appears to be empty or could not be parsed"
            )
        
        # Split text into chunks
        chunks = split_text_into_chunks(text_content)
        
        if not chunks:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No content could be extracted from the file"
            )
        
        # Generate embeddings for each chunk
        embeddings = []
        metadatas = []
        ids = []
        
        for i, chunk in enumerate(chunks):
            try:
                embedding = generate_embeddings(chunk)
                embeddings.append(embedding)
                
                # Create metadata
                metadata = {
                    "filename": file.filename,
                    "user_id": current_user.id,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                }
                metadatas.append(metadata)
                
                # Create unique ID for the chunk
                chunk_id = f"{current_user.id}_{file.filename}_{i}_{uuid.uuid4().hex[:8]}"
                ids.append(chunk_id)
                
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error processing chunk {i}: {str(e)}"
                )
        
        # Add documents to vector store
        vector_store.add_documents(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        # Save document info to database
        db_document = Document(
            filename=f"{uuid.uuid4().hex}_{file.filename}",
            original_filename=file.filename,
            file_size=file_size,
            file_type=file_extension,
            chunks_count=len(chunks),
            user_id=current_user.id
        )
        
        db.add(db_document)
        db.commit()
        db.refresh(db_document)
        
        return UploadResponse(
            message="File processed successfully",
            chunks_processed=len(chunks)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing file: {str(e)}"
        )

def extract_pdf_text(pdf_content: bytes) -> str:
    """Extract text from PDF content."""
    try:
        pdf_file = io.BytesIO(pdf_content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text.strip()
    except Exception as e:
        raise Exception(f"Error extracting PDF text: {str(e)}") 
import openai
from typing import List
import re
from app.core.config import settings

# Configure OpenAI client
openai.api_key = settings.openai_api_key

def generate_embeddings(text: str) -> List[float]:
    """Generate embeddings for given text using OpenAI."""
    try:
        response = openai.embeddings.create(
            input=text,
            model=settings.embedding_model
        )
        return response.data[0].embedding
    except Exception as e:
        raise Exception(f"Error generating embeddings: {str(e)}")

def get_llm_response(question: str, context: str) -> str:
    """Get LLM response using OpenAI with context."""
    try:
        prompt = f"""You are a helpful assistant. Use the following context to answer the question. If you don't know the answer, say you don't know.

Context: {context}

Question: {question}"""

        response = openai.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error getting LLM response: {str(e)}")

def split_text_into_chunks(text: str) -> List[str]:
    """Split text into chunks with overlap."""
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + settings.chunk_size
        
        # If this is not the last chunk, try to break at a sentence boundary
        if end < len(text):
            # Look for sentence endings within the last 100 characters of the chunk
            search_start = max(start, end - 100)
            sentence_end = text.rfind('.', search_start, end)
            if sentence_end > start:
                end = sentence_end + 1
        
        chunk = text[start:end].strip()
        if chunk:  # Only add non-empty chunks
            chunks.append(chunk)
        
        # Move start position with overlap
        start = end - settings.chunk_overlap
        if start >= len(text):
            break
    
    return chunks 
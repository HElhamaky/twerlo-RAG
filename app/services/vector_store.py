import chromadb
from chromadb.config import Settings
from typing import List, Dict
import uuid
from app.core.config import settings
import os

class VectorStore:
    def __init__(self):
        """Initialize ChromaDB client with persistent storage."""
        # Ensure the directory exists
        os.makedirs(settings.chroma_db_path, exist_ok=True)
        
        self.client = chromadb.PersistentClient(
            path=settings.chroma_db_path,
            settings=Settings(anonymized_telemetry=False)
        )
    
    def add_documents(
        self, 
        documents: List[str], 
        embeddings: List[List[float]], 
        metadatas: List[Dict], 
        ids: List[str], 
        collection_name: str = "documents"
    ) -> None:
        """Add documents and their embeddings to ChromaDB."""
        try:
            # Get or create collection
            collection = self.client.get_or_create_collection(name=collection_name)
            
            # Add documents to collection
            collection.add(
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
        except Exception as e:
            raise Exception(f"Error adding documents to vector store: {str(e)}")
    
    def similarity_search(
        self, 
        query_embedding: List[float], 
        k: int, 
        user_id: int, 
        collection_name: str = "documents"
    ) -> List[str]:
        """Search for similar documents filtered by user_id."""
        try:
            collection = self.client.get_collection(name=collection_name)
            
            # Query with user_id filter
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=k,
                where={"user_id": user_id}
            )
            
            # Return document contents
            return results['documents'][0] if results['documents'] else []
        except Exception as e:
            raise Exception(f"Error searching vector store: {str(e)}")
    
    def get_collection_names(self) -> List[str]:
        """Get all collection names."""
        try:
            return [col.name for col in self.client.list_collections()]
        except Exception as e:
            raise Exception(f"Error getting collection names: {str(e)}")

# Global vector store instance
vector_store = VectorStore() 
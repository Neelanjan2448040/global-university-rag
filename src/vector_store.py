import faiss
import numpy as np


class FAISSVectorStore:
    """FAISS-based vector store for similarity search"""
    
    def __init__(self, dim):
        """
        Initialize FAISS index.
        
        Args:
            dim: Dimension of the embeddings
        """
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, embeddings, documents):
        """
        Add embeddings and documents to the store.
        
        Args:
            embeddings: NumPy array of embeddings
            documents: List of document dictionaries
        """
        embeddings_array = np.array(embeddings).astype('float32')
        self.index.add(embeddings_array)
        self.documents.extend(documents)

    def search(self, query_embedding, k=5):
        """
        Search for top-k similar documents.
        
        Args:
            query_embedding: Query embedding vector
            k: Number of results to return
            
        Returns:
            List of top-k most similar documents
        """
        query_array = np.array([query_embedding]).astype('float32')
        D, I = self.index.search(query_array, k)
        results = [self.documents[i] for i in I[0] if i < len(self.documents)]
        return results
    
    def get_size(self):
        """Return the number of documents in the store"""
        return len(self.documents)
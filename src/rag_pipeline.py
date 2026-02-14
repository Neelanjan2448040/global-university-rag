from .embedder import embed_texts
from .vector_store import FAISSVectorStore
from .llm import generate_answer
import numpy as np


def build_store(documents):
    """Build FAISS vector store from chunked documents"""
    if not documents:
        raise ValueError("No documents provided to build the vector store.")

    print(f"Building store with {len(documents)} documents...")
    texts = [doc["text"] for doc in documents]

    # Generate embeddings
    print("Generating embeddings...")
    embeddings = embed_texts(texts)

    if len(embeddings) == 0:
        raise ValueError("Embedding generation failed.")

    # Ensure embeddings are 2D array
    if len(embeddings.shape) == 1:
        embeddings = embeddings.reshape(1, -1)
    
    dim = embeddings.shape[1]
    print(f"Embedding dimension: {dim}")

    # Initialize FAISS store
    store = FAISSVectorStore(dim)

    # Add embeddings and documents
    store.add(embeddings, documents)

    print(f"✓ Vector store built with {store.get_size()} documents (dim={dim})")
    
    return store


def answer_query(store, question, k=5):
    """Retrieve top-k relevant chunks and generate answer using LLM"""
    if not question or not question.strip():
        return "Please enter a valid question.", []

    try:
        print(f"Processing query: {question}")
        
        # Embed query
        query_embedding = embed_texts([question])
        print(f"Query embedding shape: {query_embedding.shape}")
        
        # Handle embedding shape
        if len(query_embedding.shape) == 1:
            query_embedding = query_embedding.reshape(1, -1)
        
        query_vector = query_embedding[0]
        print(f"Query vector shape: {query_vector.shape}")

        # Search in FAISS
        results = store.search(query_vector, k=k)
        print(f"Found {len(results)} results")

        if not results:
            return "No relevant information found in the knowledge base.", []

        # Build context for LLM
        context_blocks = []
        for i, r in enumerate(results, 1):
            # Extract metadata safely
            metadata = r.get('metadata', {})
            university = metadata.get('university', 'Unknown')
            section = metadata.get('section', 'Unknown')
            text_content = r.get('text', '')
            
            block = (
                f"[Source {i}]\n"
                f"University: {university}\n"
                f"Section: {section}\n"
                f"Content: {text_content}\n"
            )
            context_blocks.append(block)
            print(f"Source {i}: {university} - {section[:50]}...")

        context = "\n\n".join(context_blocks)
        print(f"Context length: {len(context)} characters")

        # Generate answer from LLM
        print("Generating answer...")
        answer = generate_answer(context, question)
        print(f"Answer generated: {answer[:100]}...")

        return answer, results
    
    except Exception as e:
        error_msg = f"Error processing query: {str(e)}"
        print(error_msg)
        import traceback
        traceback.print_exc()
        return error_msg, []
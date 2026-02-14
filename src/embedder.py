from sentence_transformers import SentenceTransformer

# Load model once at module level
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    """
    Generate embeddings for a list of texts.
    
    Args:
        texts: List of text strings or single text string
        
    Returns:
        NumPy array of embeddings
    """
    # Handle single string input
    if isinstance(texts, str):
        texts = [texts]
    
    return model.encode(texts, show_progress_bar=False)
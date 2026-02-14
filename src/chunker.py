def chunk_text(text, chunk_size=400, overlap=50):
    """
    Split text into overlapping chunks.
    
    Args:
        text: Input text to chunk
        chunk_size: Number of words per chunk
        overlap: Number of words to overlap between chunks
        
    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks


def create_chunks(valid_data):
    """
    Create chunks from validated data.
    
    Args:
        valid_data: List of validated document dictionaries
        
    Returns:
        List of chunked documents with metadata
    """
    chunked_docs = []

    for item in valid_data:
        chunks = chunk_text(item["content"])

        for chunk in chunks:
            chunked_docs.append({
                "text": chunk,
                "metadata": {
                    "url": item["url"],
                    "university": item["university"],
                    "section": item["section"],
                    "title": item["title"]
                }
            })

    return chunked_docs
# Placeholder RAG service - implement ingestion, chunking, embeddings, search here.
def retrieve_docs(query, top_k=3):
    # Return mocked docs for now
    return [
        {'id': 'doc1', 'text': 'Sample doc content 1', 'source': 'uploaded_file.pdf', 'page': 1},
        {'id': 'doc2', 'text': 'Sample doc content 2', 'source': 'uploaded_file.pdf', 'page': 2},
    ][:top_k]

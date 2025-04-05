import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index and model
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_index.bin")
doc_ids = np.load("doc_ids.npy")

# Load document texts
DATA_DIR = "data"
documents = [open(os.path.join(DATA_DIR, f"sample.txt"), "r", encoding="utf-8").read()]

def retrieve_relevant_docs(query, top_k=2):
    query_embedding = np.array([model.encode(query)])
    distances, indices = index.search(query_embedding, top_k)
    
    results = [documents[i] for i in indices[0]]
    return results

# Test retrieval
query = "What is machine learning?"
retrieved_docs = retrieve_relevant_docs(query)
print("Retrieved Documents:", retrieved_docs)

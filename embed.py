import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Directory where text files are stored
DATA_DIR = "data"

# Read and embed documents
documents = []
doc_ids = []

for idx, filename in enumerate(os.listdir(DATA_DIR)):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as file:
        text = file.read()
        documents.append(text)
        doc_ids.append(idx)

# Convert texts to embeddings
doc_embeddings = np.array([model.encode(doc) for doc in documents])

# Store in FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# Save index
faiss.write_index(index, "faiss_index.bin")
np.save("doc_ids.npy", np.array(doc_ids))
print("Embeddings stored successfully!")

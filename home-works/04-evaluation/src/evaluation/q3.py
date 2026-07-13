from pathlib import Path
import sys

# Add ../src to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import VectorSearch

# Load embedder
embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

# Load lesson pages
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [doc.parse() for doc in reader.read()]

# Create chunks
chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# Build embeddings
texts = [chunk["content"] for chunk in chunks]
vectors = np.array(embedder.encode_batch(texts))

# Build vector index
index = VectorSearch(
    keyword_fields=["filename"]
)

index.fit(vectors, chunks)

# Load ground truth
ground_truth = pd.read_csv("data/ground-truth.csv").to_dict(orient="records")

# First question
q = ground_truth[0]["question"]

print("\nQuestion:")
print(q)

# Embed query
query_vector = embedder.encode(q)

# Search
results = index.search(
    query_vector=query_vector,
    num_results=5
)

print("\nTop results:\n")

for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc['filename']}")
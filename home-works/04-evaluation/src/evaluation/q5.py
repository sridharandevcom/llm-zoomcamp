from pathlib import Path
import sys

# Allow importing from src/
sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import VectorSearch

# ----------------------------
# Load embedder
# ----------------------------

embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

# ----------------------------
# Load lesson pages
# ----------------------------

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [doc.parse() for doc in reader.read()]

# ----------------------------
# Create chunks
# ----------------------------

chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# ----------------------------
# Build embeddings
# ----------------------------

texts = [chunk["content"] for chunk in chunks]
vectors = np.array(embedder.encode_batch(texts))

print("Embedding matrix:", vectors.shape)

# ----------------------------
# Build vector index
# ----------------------------

vector_index = VectorSearch(
    keyword_fields=["filename"]
)

vector_index.fit(vectors, chunks)

# ----------------------------
# Load ground truth
# ----------------------------

ground_truth = pd.read_csv(
    "data/ground-truth.csv"
).to_dict(orient="records")

# ----------------------------
# Vector search function
# ----------------------------

def vector_search(query, num_results=5):
    query_vector = embedder.encode(query)

    return vector_index.search(
        query_vector=query_vector,
        num_results=num_results
    )

# ----------------------------
# Evaluation functions
# ----------------------------

def compute_relevance(record):
    expected = record["filename"]

    results = vector_search(record["question"])

    relevance = [
        1 if doc["filename"] == expected else 0
        for doc in results
    ]

    return relevance


def hit_rate(relevances):
    return sum(any(r) for r in relevances) / len(relevances)


def mrr(relevances):
    score = 0.0

    for rel in relevances:
        for rank, value in enumerate(rel):
            if value:
                score += 1 / (rank + 1)
                break

    return score / len(relevances)


# ----------------------------
# Run evaluation
# ----------------------------

relevances = [
    compute_relevance(record)
    for record in ground_truth
]

print("\nVector Search Evaluation")
print("------------------------")
print(f"Hit Rate: {hit_rate(relevances):.4f}")
print(f"MRR:      {mrr(relevances):.4f}")
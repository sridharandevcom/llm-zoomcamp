from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index, VectorSearch

# ----------------------------
# Load documents
# ----------------------------

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [doc.parse() for doc in reader.read()]

chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# ----------------------------
# Text index
# ----------------------------

text_index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

text_index.fit(chunks)

# ----------------------------
# Vector index
# ----------------------------

embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

texts = [chunk["content"] for chunk in chunks]
vectors = np.array(embedder.encode_batch(texts))

vector_index = VectorSearch(
    keyword_fields=["filename"]
)

vector_index.fit(vectors, chunks)

# ----------------------------
# Search functions
# ----------------------------

def text_search(query, num_results=10):
    return text_index.search(
        query=query,
        num_results=num_results
    )


def vector_search(query, num_results=10):
    query_vector = embedder.encode(query)

    return vector_index.search(
        query_vector=query_vector,
        num_results=num_results
    )


# ----------------------------
# Reciprocal Rank Fusion
# ----------------------------

def rrf(result_lists, k=60, num_results=5):
    scores = {}
    docs = {}

    for results in result_lists:
        for rank, doc in enumerate(results):
            key = (doc["filename"], doc["start"])
            scores[key] = scores.get(key, 0) + 1 / (k + rank)
            docs[key] = doc

    ranked = sorted(scores, key=scores.get, reverse=True)
    return [docs[key] for key in ranked[:num_results]]


def hybrid_search(query, k):
    text_results = text_search(query, num_results=10)
    vector_results = vector_search(query, num_results=10)

    return rrf([text_results, vector_results], k=k)


# ----------------------------
# Evaluation
# ----------------------------

ground_truth = pd.read_csv(
    "data/ground-truth.csv"
).to_dict(orient="records")


def evaluate(search_fn):
    relevances = []

    for record in ground_truth:
        expected = record["filename"]

        results = search_fn(record["question"])

        rel = [
            1 if doc["filename"] == expected else 0
            for doc in results
        ]

        relevances.append(rel)

    hit_rate = sum(any(r) for r in relevances) / len(relevances)

    mrr = 0

    for rel in relevances:
        for rank, value in enumerate(rel):
            if value:
                mrr += 1 / (rank + 1)
                break

    mrr /= len(relevances)

    return hit_rate, mrr


for k in [1, 50, 100, 200]:
    hr, mrr = evaluate(
        lambda q: hybrid_search(q, k)
    )

    print(f"k={k:3d}  Hit Rate={hr:.4f}  MRR={mrr:.4f}")
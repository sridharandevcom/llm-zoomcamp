import numpy as np
import pandas as pd

from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index

# Load documents
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [f.parse() for f in reader.read()]

# Chunk documents
chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print("Chunks:", len(chunks))

# Build text index
index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(chunks)

# Load ground truth
ground_truth = pd.read_csv("data/ground-truth.csv").to_dict(orient="records")

# First question
q = ground_truth[0]["question"]

print("\nQuestion:")
print(q)

results = index.search(
    query=q,
    num_results=5
)

print("\nTop results:\n")

for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc['filename']}")
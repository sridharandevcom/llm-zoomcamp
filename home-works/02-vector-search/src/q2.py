import numpy as np

from embedder import Embedder
from gitsource import GithubRepositoryDataReader

# Load embedder
embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

# Query embedding
query = "How does approximate nearest neighbor search work?"
query_vector = embedder.encode(query)

# Load lesson pages
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [file.parse() for file in reader.read()]

# Find the target lesson
target = None

for doc in documents:
    if doc["filename"] == "02-vector-search/lessons/07-sqlitesearch-vector.md":
        target = doc
        break

if target is None:
    raise ValueError("Lesson not found")

# Embed lesson content
doc_vector = embedder.encode(target["content"])

# Cosine similarity = dot product
similarity = np.dot(query_vector, doc_vector)

print("Cosine similarity:", similarity)
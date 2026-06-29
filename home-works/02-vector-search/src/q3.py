import numpy as np

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents

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

# Chunk documents
chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# Embed all chunk contents
texts = [chunk["content"] for chunk in chunks]
X = np.array(embedder.encode_batch(texts))

# Compute similarities
scores = X.dot(query_vector)

# Find best match
best_idx = np.argmax(scores)
best_chunk = chunks[best_idx]

print("\nBest filename:")
print(best_chunk["filename"])

print("\nScore:")
print(scores[best_idx])
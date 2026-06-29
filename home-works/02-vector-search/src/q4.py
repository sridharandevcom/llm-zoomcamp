import numpy as np

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

documents = [file.parse() for file in reader.read()]

# Chunk documents
chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# Embed all chunks
texts = [chunk["content"] for chunk in chunks]
vectors = np.array(embedder.encode_batch(texts))

print(f"Vectors shape: {vectors.shape}")

# Build vector index
index = VectorSearch(
    keyword_fields=["filename"]
)

index.fit(vectors, chunks)

# Embed query
query = "What metric do we use to evaluate a search engine?"
query_vector = embedder.encode(query)

# Search
results = index.search(
    query_vector=query_vector,
    num_results=5
)

print("\nTop results:\n")

for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc['filename']}")
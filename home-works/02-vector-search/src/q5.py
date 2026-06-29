import numpy as np

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index, VectorSearch

# Load embedder
embedder = Embedder("models/Xenova/all-MiniLM-L6-v2")

# Load documents
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

query = "How do I store vectors in PostgreSQL?"

# -----------------------
# Text Search
# -----------------------
text_index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

text_index.fit(chunks)

text_results = text_index.search(
    query=query,
    num_results=5
)

# -----------------------
# Vector Search
# -----------------------
texts = [chunk["content"] for chunk in chunks]
vectors = np.array(embedder.encode_batch(texts))

vector_index = VectorSearch(
    keyword_fields=["filename"]
)

vector_index.fit(vectors, chunks)

query_vector = embedder.encode(query)

vector_results = vector_index.search(
    query_vector=query_vector,
    num_results=5
)

print("TEXT SEARCH")
text_files = []

for doc in text_results:
    print(doc["filename"])
    text_files.append(doc["filename"])

print("\nVECTOR SEARCH")
vector_files = []

for doc in vector_results:
    print(doc["filename"])
    vector_files.append(doc["filename"])

print("\nOnly in vector search:")

for f in vector_files:
    if f not in text_files:
        print(f)
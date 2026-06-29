import numpy as np

from embedder import Embedder
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index, VectorSearch


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

query = "How do I give the model access to tools?"

# ------------------------
# Text Search
# ------------------------

text_index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

text_index.fit(chunks)

text_results = text_index.search(
    query=query,
    num_results=5
)

# ------------------------
# Vector Search
# ------------------------

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

# ------------------------
# Hybrid (RRF)
# ------------------------

results = rrf([vector_results, text_results])

print("Hybrid results:\n")

for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc['filename']}")
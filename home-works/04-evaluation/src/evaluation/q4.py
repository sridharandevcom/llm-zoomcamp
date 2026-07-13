import pandas as pd

from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index

# ------------------------
# Load documents
# ------------------------

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

print("Chunks:", len(chunks))

# ------------------------
# Build text index
# ------------------------

index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(chunks)

# ------------------------
# Search function
# ------------------------

def text_search(query, num_results=5):
    return index.search(
        query=query,
        num_results=num_results
    )

# ------------------------
# Load ground truth
# ------------------------

ground_truth = pd.read_csv(
    "data/ground-truth.csv"
).to_dict(orient="records")

# ------------------------
# Evaluation
# ------------------------

def compute_relevance(record):
    question = record["question"]
    expected = record["filename"]

    results = text_search(question)

    relevance = [
        1 if doc["filename"] == expected else 0
        for doc in results
    ]

    return relevance


def hit_rate(relevances):
    return sum(any(r) for r in relevances) / len(relevances)


def mrr(relevances):
    total = 0

    for rel in relevances:
        for rank, value in enumerate(rel):
            if value:
                total += 1 / (rank + 1)
                break

    return total / len(relevances)


relevances = [
    compute_relevance(record)
    for record in ground_truth
]

print("\nHit Rate:", hit_rate(relevances))
print("MRR:", mrr(relevances))
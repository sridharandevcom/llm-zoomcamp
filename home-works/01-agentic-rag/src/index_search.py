from gitsource import GithubRepositoryDataReader
from minsearch import Index

# Load lesson pages
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [f.parse() for f in reader.read()]

print(f"Loaded {len(documents)} documents")

# Create the search index
index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(documents)

# Test query
query = "How does the agentic loop keep calling the model until it stops?"

results = index.search(
    query=query,
    num_results=5
)

print("\nTop results:")
for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc['filename']}")
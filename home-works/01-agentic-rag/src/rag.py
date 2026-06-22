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

# Build index
index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(documents)

# User question
question = "How does the agentic loop keep calling the model until it stops?"

# Retrieve context
results = index.search(
    query=question,
    num_results=3
)

# Build context string
context = "\n\n".join(
    f"FILE: {doc['filename']}\n{doc['content'][:1000]}"
    for doc in results
)

prompt = f"""
You are a teaching assistant for the LLM Zoomcamp course.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

print(prompt[:3000])
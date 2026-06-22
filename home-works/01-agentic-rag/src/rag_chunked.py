from openai import OpenAI
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index
from rag_helper import RAGBase

# Load lesson pages
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [f.parse() for f in reader.read()]

# Create chunks
chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

# Build index on chunks
index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(chunks)

client = OpenAI()

rag = RAGBase(
    index=index,
    llm_client=client,
    model="gpt-5.4-mini"
)

question = "How does the agentic loop keep calling the model until it stops?"

answer, usage = rag.rag(question)

print("\nAnswer:")
print(answer)

print("\nUsage:")
print(usage)
print(f"\nInput tokens: {usage.input_tokens}")
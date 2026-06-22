from openai import OpenAI
from gitsource import GithubRepositoryDataReader, chunk_documents
from minsearch import Index
from toyaikit import Agent

# Load documents
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

# Build chunk index
index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(chunks)

client = OpenAI()

search_calls = 0


def search(query: str) -> str:
    """
    Search the course lessons and return relevant content.
    """
    global search_calls
    search_calls += 1

    results = index.search(
        query=query,
        num_results=3
    )

    context = []

    for doc in results:
        context.append(
            f"FILE: {doc['filename']}\n{doc['content']}"
        )

    return "\n\n".join(context)


agent = Agent(
    client=client,
    model="gpt-5.4-mini",
    instructions=(
        "You're a course teaching assistant. "
        "Answer the student's question using the search tool. "
        "Make multiple searches with different keywords before answering."
    ),
    tools=[search]
)

question = (
    "How does the agentic loop work, "
    "and how is it different from plain RAG?"
)

answer = agent.run(question)

print(answer)
print()
print("Search calls:", search_calls)
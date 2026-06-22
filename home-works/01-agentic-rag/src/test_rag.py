from openai import OpenAI
from gitsource import GithubRepositoryDataReader
from minsearch import Index
from rag_helper import RAGBase

client = OpenAI()

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [f.parse() for f in reader.read()]

index = Index(
    text_fields=["content"],
    keyword_fields=["filename"]
)

index.fit(documents)

rag = RAGBase(
    index=index,
    llm_client=client,
    model="gpt-5.4-mini"
)

question = "How does the agentic loop keep calling the model until it stops?"

answer, usage = rag.rag(question)

print(answer)
print()
print("Usage:")
print(usage)
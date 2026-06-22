from gitsource import GithubRepositoryDataReader, chunk_documents

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [f.parse() for f in reader.read()]

print(f"Documents: {len(documents)}")

chunks = chunk_documents(
    documents,
    size=2000,
    step=1000
)

print(f"Chunks: {len(chunks)}")

print("\nFirst chunk keys:")
print(chunks[0].keys())
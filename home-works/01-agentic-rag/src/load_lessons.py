from gitsource import GithubRepositoryDataReader

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

files = reader.read()
documents = [f.parse() for f in files]

print("Number of documents:", len(documents))
print("Keys:", documents[0].keys())
print("First file:", documents[0]["filename"])
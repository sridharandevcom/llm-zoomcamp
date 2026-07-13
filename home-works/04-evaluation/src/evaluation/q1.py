import json

from openai import OpenAI
from dotenv import load_dotenv

from gitsource import GithubRepositoryDataReader
from evaluation_utils import llm_structured
from pydantic import BaseModel

load_dotenv()

client = OpenAI()


class Questions(BaseModel):
    questions: list[str]


data_gen_instructions = """
You emulate a student who is taking our LLM course.

You are given one lesson page from the course.

Formulate 5 questions this student might ask that are answered by this page.

Rules:
- The page should contain the answer to each question.
- Make the questions complete and not too short.
- Use as few words as possible from the page; don't copy its phrasing.
- The questions should resemble how people actually ask things online:
  not too formal, not too short, not too long.
- Ask about the content of the lesson, not about its formatting or filename.
""".strip()


reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [file.parse() for file in reader.read()]

pages = documents[:3]

input_tokens = []

for page in pages:
    user_prompt = json.dumps(
        {
            "filename": page["filename"],
            "content": page["content"],
        },
        indent=2,
    )

    questions, usage = llm_structured(
        client=client,
        instructions=data_gen_instructions,
        user_prompt=user_prompt,
        output_type=Questions,
        model="gpt-5.4-mini",
    )

    print(page["filename"])
    print("Input tokens:", usage.input_tokens)
    print()

    input_tokens.append(usage.input_tokens)

average = sum(input_tokens) / len(input_tokens)

print("=" * 50)
print(f"Average input tokens: {average:.2f}")
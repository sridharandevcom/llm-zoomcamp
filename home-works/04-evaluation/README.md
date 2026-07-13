# LLM Zoomcamp 2026 - Homework 4: Evaluation

This repository contains my implementation for Homework 4 of the DataTalks.Club LLM Zoomcamp 2026 course.

## Objectives

The goal of this homework is to evaluate different search approaches by generating and using a ground truth dataset. The implementation covers:

- Generating evaluation questions using an LLM
- Loading a pre-generated ground truth dataset
- Building a text search index
- Building a vector search index
- Implementing hybrid search using Reciprocal Rank Fusion (RRF)
- Evaluating search quality using Hit Rate and Mean Reciprocal Rank (MRR)
- Comparing keyword, vector, and hybrid search approaches

## Technologies Used

- Python 3
- openai
- pydantic
- python-dotenv
- pandas
- numpy
- gitsource
- minsearch
- onnxruntime
- tokenizers

## Project Structure

```text
04-evaluation/
│
├── .venv/
├── data/
│   └── ground-truth.csv
├── models/
│   └── Xenova/
│       └── all-MiniLM-L6-v2/
├── src/
│   ├── download.py
│   ├── embedder.py
│   └── evaluation/
│       ├── rag_helper.py
│       ├── evaluation_utils.py
│       ├── q1.py
│       ├── q2.py
│       ├── q3.py
│       ├── q4.py
│       ├── q5.py
│       └── q6.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Implementation Overview

### Data Loading

- Load lesson pages directly from the course GitHub repository.
- Restrict loading to lesson markdown files.
- Parse documents into a structured format.

### Ground Truth Generation

- Generate evaluation questions using an LLM.
- Associate each generated question with its corresponding lesson page.
- Load the provided ground truth dataset for evaluation.

### Search Indexes

- Build a keyword search index.
- Build a vector search index using ONNX embeddings.
- Create a hybrid search implementation using Reciprocal Rank Fusion (RRF).

### Search Evaluation

- Evaluate retrieval performance using:
  - Hit Rate
  - Mean Reciprocal Rank (MRR)
- Compare text, vector, and hybrid search approaches across the complete evaluation dataset.

## Running the Scripts

```bash
python src/evaluation/q1.py
python src/evaluation/q2.py
python src/evaluation/q3.py
python src/evaluation/q4.py
python src/evaluation/q5.py
python src/evaluation/q6.py
```

## References

- DataTalks.Club LLM Zoomcamp 2026
- Module 4: Evaluation
- Homework 4 Instructions
- LLM Zoomcamp GitHub Repository
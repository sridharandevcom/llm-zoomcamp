# LLM Zoomcamp 2026 - Homework 2: Vector Search

This repository contains my implementation for Homework 2 of the DataTalks.Club LLM Zoomcamp 2026 course.

## Objectives

The goal of this homework is to build a semantic search system by progressively implementing:

* Generating text embeddings using the ONNX Embedder
* Computing cosine similarity between embeddings
* Chunking lesson documents for improved retrieval
* Implementing manual vector search
* Building a vector search index with MinSearch
* Comparing keyword search with vector search
* Implementing hybrid search using Reciprocal Rank Fusion (RRF)

## Technologies Used

* Python 3
* `onnxruntime`
* `tokenizers`
* `gitsource`
* `minsearch`
* `numpy`
* `tqdm`
* `huggingface-hub`
* `jupyter`

## Project Structure

```text
02-vector-search/
├── src/
│   ├── download.py
│   ├── embedder.py
│   ├── q1.py
│   ├── q2.py
│   ├── q3.py
│   ├── q4.py
│   ├── q5.py
│   └── q6.py
├── models/
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

## Download the Embedding Model

Download the helper scripts:

```bash
python src/download.py
```

This downloads the ONNX version of the **all-MiniLM-L6-v2** embedding model into the `models/` directory.

## Implementation Overview

### Query Embeddings

* Generate dense vector representations for natural language queries.
* Use the lightweight ONNX embedding model.

### Cosine Similarity

* Compute semantic similarity between query embeddings and document embeddings.
* Use the dot product since the embeddings are normalized.

### Document Chunking

* Split lesson pages into overlapping chunks.
* Preserve metadata required for retrieval.

### Manual Vector Search

* Embed all document chunks.
* Build a vector matrix.
* Perform similarity search using matrix multiplication.

### Vector Search with MinSearch

* Build a vector index using MinSearch.
* Retrieve the most semantically similar document chunks.

### Text Search vs. Vector Search

* Compare keyword-based retrieval with semantic retrieval.
* Observe the strengths and limitations of both approaches.

### Hybrid Search

* Combine keyword search and vector search.
* Merge ranked results using Reciprocal Rank Fusion (RRF).

## Running the Scripts

```bash
python src/q1.py
python src/q2.py
python src/q3.py
python src/q4.py
python src/q5.py
python src/q6.py
```

## References

* DataTalks.Club LLM Zoomcamp 2026
* Module 2: Vector Search
* Homework 2 Instructions
* LLM Zoomcamp GitHub Repository

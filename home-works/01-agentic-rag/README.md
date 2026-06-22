# LLM Zoomcamp 2026 - Homework 1: Agentic RAG

This repository contains my implementation for Homework 1 of the DataTalks.Club LLM Zoomcamp 2026 course.

## Objectives

The goal of this homework is to build an Agentic Retrieval-Augmented Generation (RAG) system by progressively implementing:

* Loading lesson documents from a GitHub repository
* Building a search index
* Implementing a basic RAG pipeline
* Applying document chunking
* Building a chunk-based RAG system
* Creating an agent that can iteratively use search tools

## Technologies Used

* Python 3
* `gitsource`
* `minsearch`
* `openai`
* `python-dotenv`
* `jupyter`
* `requests`
* `numpy`
* `pandas`

## Project Structure

```text
01-agentic-rag/
│
├── .venv/
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   ├── load_lessons.py
│   ├── index_search.py
│   ├── rag_helper.py
│   ├── rag.py
│   ├── chunking.py
│   ├── rag_chunked.py
│   └── agent.py
└── notebooks/
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

### Document Loading

* Load lesson markdown files directly from the course GitHub repository.
* Restrict loading to lesson files only.
* Parse the documents into a searchable format.

### Indexing and Search

* Create a search index over the lesson contents.
* Support keyword-based retrieval of relevant lesson pages.

### Retrieval-Augmented Generation (RAG)

* Retrieve relevant documents for a user query.
* Build prompts from retrieved context.
* Generate answers using an LLM.

### Document Chunking

* Split lesson files into overlapping chunks.
* Preserve metadata required for retrieval.

### Chunk-Based RAG

* Build an index on document chunks.
* Retrieve smaller and more focused contexts.
* Compare retrieval efficiency with the original implementation.

### Agentic RAG

* Expose search as a tool.
* Allow the model to decide when and what to search.
* Implement an iterative search-and-reason workflow.

## Running the Scripts

```bash# LLM Zoomcamp 2026 - Homework 1: Agentic RAG

This repository contains my implementation for Homework 1 of the DataTalks.Club LLM Zoomcamp 2026 course.

## Objectives

The goal of this homework is to build an Agentic Retrieval-Augmented Generation (RAG) system by progressively implementing:

* Loading lesson documents from a GitHub repository
* Building a search index
* Implementing a basic RAG pipeline
* Applying document chunking
* Building a chunk-based RAG system
* Creating an agent that can iteratively use search tools

## Technologies Used

* Python 3
* `gitsource`
* `minsearch`
* `openai`
* `python-dotenv`
* `jupyter`
* `requests`
* `numpy`
* `pandas`

## Project Structure

```text
01-agentic-rag/
│
├── .venv/
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   ├── load_lessons.py
│   ├── index_search.py
│   ├── rag_helper.py
│   ├── rag.py
│   ├── chunking.py
│   ├── rag_chunked.py
│   └── agent.py
└── notebooks/
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

### Document Loading

* Load lesson markdown files directly from the course GitHub repository.
* Restrict loading to lesson files only.
* Parse the documents into a searchable format.

### Indexing and Search

* Create a search index over the lesson contents.
* Support keyword-based retrieval of relevant lesson pages.

### Retrieval-Augmented Generation (RAG)

* Retrieve relevant documents for a user query.
* Build prompts from retrieved context.
* Generate answers using an LLM.

### Document Chunking

* Split lesson files into overlapping chunks.
* Preserve metadata required for retrieval.

### Chunk-Based RAG

* Build an index on document chunks.
* Retrieve smaller and more focused contexts.
* Compare retrieval efficiency with the original implementation.

### Agentic RAG

* Expose search as a tool.
* Allow the model to decide when and what to search.
* Implement an iterative search-and-reason workflow.

## Running the Scripts

```bash
python src/load_lessons.py
python src/index_search.py
python src/rag.py
python src/chunking.py
python src/rag_chunked.py
python src/agent.py
```

## References

* DataTalks.Club LLM Zoomcamp 2026
* Module 1: Agentic RAG
* Homework 1 Instructions
* LLM Zoomcamp GitHub Repository

python src/load_lessons.py
python src/index_search.py
python src/rag.py
python src/chunking.py
python src/rag_chunked.py
python src/agent.py
```

## References

* DataTalks.Club LLM Zoomcamp 2026
* Module 1: Agentic RAG
* Homework 1 Instructions
* LLM Zoomcamp GitHub Repository

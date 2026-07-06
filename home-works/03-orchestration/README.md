# LLM Zoomcamp 2026 - Homework 3: Orchestration

This repository contains my implementation for Homework 3 of the DataTalks.Club LLM Zoomcamp 2026 course.

## Objectives

The goal of this homework is to explore AI workflow orchestration using Kestra by progressively implementing:

* Executing AI-powered workflows with Kestra
* Comparing responses with and without Retrieval-Augmented Generation (RAG)
* Measuring token usage for different prompt configurations
* Modifying AI workflow prompts
* Understanding the impact of prompt design on token consumption
* Exploring deterministic workflows and AI agent orchestration

## Technologies Used

* Python 3
* Kestra
* Gemini API
* OpenAI API
* Tavily API (optional)
* YAML
* Docker
* Retrieval-Augmented Generation (RAG)

## Project Structure

```text
03-orchestration/
├── flows/
│   ├── 1_chat_without_rag.yaml
│   ├── 2_chat_with_rag.yaml
│   ├── 3_web_search_agent.yaml
│   ├── 4_simple_agent.yaml
│   └── ...
├── data/
├── .env
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Prerequisites

* Docker Desktop
* Kestra
* Gemini API Key
* OpenAI API Key (for selected workflows)
* Tavily API Key (optional)

## Setup

### Clone the repository

```bash
git clone https://github.com/DataTalksClub/llm-zoomcamp.git
```

### Start Kestra

```bash
docker compose up -d
```

### Configure Environment Variables

Create a `.env` file and configure the required API keys.

Example:

```env
GEMINI_API_KEY=your-gemini-api-key
SECRET_GEMINI_API_KEY=<base64-encoded-gemini-api-key>

OPENAI_API_KEY=your-openai-api-key
SECRET_OPENAI_API_KEY=<base64-encoded-openai-api-key>

TAVILY_API_KEY=your-tavily-api-key
SECRET_TAVILY_API_KEY=<base64-encoded-tavily-api-key>
```

### Open Kestra

After the containers are running, open the Kestra UI in your browser and import the workflow files.

## Implementation Overview

### Chat Without RAG

* Execute an AI workflow without retrieval.
* Observe how the model responds using only its internal knowledge.

### Chat With RAG

* Execute the workflow with document retrieval enabled.
* Compare the grounded response with the non-RAG version.

### AI Agent Workflows

* Execute agent-based workflows.
* Observe how the workflow coordinates multiple AI tasks.

### Token Usage Analysis

* Measure input and output token usage.
* Compare token consumption for different prompt lengths.

### Prompt Engineering

* Modify prompts within the workflow.
* Observe how prompt changes affect response quality and token usage.

### Workflow Orchestration

* Understand the differences between deterministic workflows and AI agents.
* Explore orchestration patterns for production AI systems.

## Running the Workflows

Run the workflows from the Kestra UI:

* `1_chat_without_rag.yaml`
* `2_chat_with_rag.yaml`
* `3_web_search_agent.yaml`
* `4_simple_agent.yaml`

Review the execution logs after each run to inspect responses, workflow behavior, and token usage.

## References

* DataTalks.Club LLM Zoomcamp 2026
* Module 3: Orchestration
* Homework 3 Instructions
* Kestra Documentation
* LLM Zoomcamp GitHub Repository

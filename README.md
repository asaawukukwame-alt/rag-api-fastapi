# RAG API with FastAPI

A Retrieval-Augmented Generation API built with Python, FastAPI, ChromaDB, Docker, GitHub Actions, and the OpenAI API.

This project demonstrates how to build a backend AI application that can ingest a document, split it into chunks, store searchable context in a vector database, retrieve relevant chunks, and generate grounded answers using an LLM.

## Project Status

- FastAPI application foundation complete
- Document ingestion and chunking complete
- ChromaDB vector storage and retrieval complete
- OpenAI-powered answer generation complete
- API error handling complete
- Automated tests with pytest complete
- Docker configuration complete
- GitHub Actions CI complete

## Tech Stack

- Python
- FastAPI
- Uvicorn
- ChromaDB
- OpenAI API
- Pydantic
- pytest
- Docker
- GitHub Actions

## Architecture

User question goes to the FastAPI `/ask` endpoint. The API retrieves relevant chunks from ChromaDB, builds a grounded prompt with that context, sends the prompt to the OpenAI model, and returns an answer with source chunks.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirms the API is running |
| GET | `/health` | Health check endpoint |
| GET | `/ingest/sample` | Loads and chunks the sample policy document |
| POST | `/index/sample` | Indexes the sample document into ChromaDB |
| GET | `/retrieve?query=...` | Retrieves relevant document chunks |
| POST | `/ask` | Generates an answer using retrieved context |

## Example Question

```json
{
  "question": "What should employees not upload into public AI tools?"
}
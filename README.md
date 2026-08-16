# RAG API with FastAPI

A Retrieval-Augmented Generation API built with Python, FastAPI, ChromaDB, Docker, GitHub Actions, and the OpenAI API.

This project demonstrates how to build a backend AI application that can ingest a document, split it into chunks, store searchable context in a vector database, retrieve relevant chunks, and generate grounded answers using an LLM.

## Live Demo

Live API documentation:

https://rag-api-fastapi-1.onrender.com/docs#/

Health check:

https://rag-api-fastapi-1.onrender.com/health

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

User question goes to the FastAPI /ask endpoint. The API retrieves relevant chunks from ChromaDB, builds a grounded prompt with that context, sends the prompt to the OpenAI model, and returns an answer with source chunks.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Confirms the API is running |
| GET | /health | Health check endpoint |
| GET | /ingest/sample | Loads and chunks the sample policy document |
| POST | /index/sample | Indexes the sample document into ChromaDB |
| GET | /retrieve?query=... | Retrieves relevant document chunks |
| POST | /ask | Generates an answer using retrieved context |

## Example Question

What should employees not upload into public AI tools?

## Example Answer

The API retrieves relevant policy context and answers that employees should not upload confidential customer data, private financial records, passwords, API keys, medical records, or legal documents into public AI tools.

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the API:

python -m uvicorn app.main:app --reload

Open the interactive API docs:

http://127.0.0.1:8000/docs

## Environment Variables

Create a .env file locally:

OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

Do not commit .env to GitHub.

## Run with Docker

Build the Docker image:

docker build -t rag-api-fastapi .

Run the container:

docker run --rm -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key_here -e OPENAI_MODEL=gpt-4o-mini rag-api-fastapi

Then open:

http://127.0.0.1:8000/docs

## Run Tests

python -m pytest

## GitHub Actions CI

This repository includes a GitHub Actions workflow that runs tests automatically on pushes and pull requests to the main branch.

## What This Project Demonstrates

- Building backend APIs with FastAPI
- Creating document ingestion pipelines
- Chunking documents for retrieval
- Using ChromaDB as a vector database
- Connecting retrieval to LLM answer generation
- Protecting API keys with environment variables
- Writing tests with pytest
- Adding Docker support
- Adding CI automation with GitHub Actions

## Future Improvements

- Support user-uploaded documents
- Add persistent document collections
- Add source citations with document metadata
- Add authentication
- Deploy to a cloud hosting platform
- Add monitoring and logging
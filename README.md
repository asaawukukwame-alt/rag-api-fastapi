# RAG API with FastAPI

A Retrieval-Augmented Generation API built with Python, FastAPI, ChromaDB, and OpenAI.

This project demonstrates how to build a backend AI application that can ingest documents, store searchable context in a vector database, retrieve relevant chunks, and generate grounded answers using an LLM.

## Project Status

- ✅ FastAPI application foundation
- ✅ Document ingestion and chunking
- ✅ ChromaDB vector storage and retrieval
- ✅ OpenAI-powered answer generation
- ✅ API error handling
- ✅ Automated tests with pytest
- ✅ Docker configuration
- ✅ GitHub Actions CI

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

```text
User Question
     |
     v
FastAPI /ask endpoint
     |
     v
Retrieve relevant chunks from ChromaDB
     |
     v
Build grounded prompt with retrieved context
     |
     v
OpenAI model generates answer
     |
     v
Return answer + source chunks
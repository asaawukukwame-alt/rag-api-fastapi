# RAG API with FastAPI

This project is a Retrieval-Augmented Generation API built with Python and FastAPI.

The goal is to build an AI application that can ingest documents, store searchable document chunks, retrieve relevant context, and generate grounded answers using an LLM.

## Project Status

Phase 1: FastAPI app foundation
Phase 2: Document ingestion
Phase 3: Vector database retrieval
Phase 4: LLM answer generation
Phase 5: Dockerization
Phase 6: GitHub Actions testing

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- OpenAI API
- ChromaDB
- Git
- GitHub

## Current Endpoints

- GET /
- GET /health

## Run Locally

Install dependencies:

    pip install -r requirements.txt

Run the API:

    python -m uvicorn app.main:app --reload

Then open:

    http://127.0.0.1:8000/health

Expected response:

    {"status":"ok"}

## Phase 1 Complete

The FastAPI foundation is working locally with a health-check endpoint.

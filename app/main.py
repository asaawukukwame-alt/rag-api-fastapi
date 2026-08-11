from fastapi import FastAPI
from app.ingest import ingest_document

app = FastAPI(
    title="RAG API with FastAPI",
    description="A Retrieval-Augmented Generation API built with Python and FastAPI.",
    version="0.2.0",
)


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/ingest/sample")
def ingest_sample_document():
    chunks = ingest_document("data/sample_policy.txt")

    return {
        "file": "data/sample_policy.txt",
        "chunk_count": len(chunks),
        "chunks": chunks,
    }

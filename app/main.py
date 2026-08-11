from fastapi import FastAPI
from app.ingest import ingest_document
from app.rag import index_sample_document, retrieve_context

app = FastAPI(
    title="RAG API with FastAPI",
    description="A Retrieval-Augmented Generation API built with Python and FastAPI.",
    version="0.3.0",
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


@app.post("/index/sample")
def index_sample():
    return index_sample_document()


@app.get("/retrieve")
def retrieve(query: str):
    return retrieve_context(query)

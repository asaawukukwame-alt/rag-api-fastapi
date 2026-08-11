from fastapi import FastAPI
from app.ingest import ingest_document
from app.rag import index_sample_document, retrieve_context, generate_answer
from app.schemas import AskRequest, AskResponse

app = FastAPI(
    title="RAG API with FastAPI",
    description="A Retrieval-Augmented Generation API built with Python and FastAPI.",
    version="0.4.0",
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


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    return generate_answer(request.question)

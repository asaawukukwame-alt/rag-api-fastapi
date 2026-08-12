from fastapi import FastAPI, HTTPException
from app.ingest import ingest_document
from app.rag import index_sample_document, retrieve_context, generate_answer
from app.schemas import AskRequest, AskResponse

app = FastAPI(
    title="RAG API with FastAPI",
    description="A Retrieval-Augmented Generation API built with Python and FastAPI.",
    version="0.5.0",
)


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/ingest/sample")
def ingest_sample_document():
    try:
        chunks = ingest_document("data/sample_policy.txt")

        return {
            "file": "data/sample_policy.txt",
            "chunk_count": len(chunks),
            "chunks": chunks,
        }

    except FileNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.post("/index/sample")
def index_sample():
    try:
        return index_sample_document()

    except FileNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {error}")


@app.get("/retrieve")
def retrieve(query: str):
    try:
        return retrieve_context(query)

    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Retrieval failed: {error}")


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        return generate_answer(request.question)

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Answer generation failed: {error}")

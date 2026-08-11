from fastapi import FastAPI

app = FastAPI(
    title="RAG API with FastAPI",
    description="A Retrieval-Augmented Generation API built with Python and FastAPI.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

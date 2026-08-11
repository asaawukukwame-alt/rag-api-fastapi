import chromadb
from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.ingest import ingest_document


CHROMA_PATH = ".chroma"
COLLECTION_NAME = "sample_policy"


def get_chroma_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection


def reset_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    try:
        client.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass

    return client.get_or_create_collection(name=COLLECTION_NAME)


def index_sample_document() -> dict:
    chunks = ingest_document("data/sample_policy.txt")
    collection = reset_collection()

    ids = [f"chunk-{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=[{"source": "data/sample_policy.txt"} for _ in chunks],
    )

    return {
        "source": "data/sample_policy.txt",
        "chunk_count": len(chunks),
        "ids": ids,
    }


def retrieve_context(query: str, n_results: int = 3) -> dict:
    collection = get_chroma_collection()

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
    )

    documents = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]

    return {
        "query": query,
        "result_count": len(documents),
        "ids": ids,
        "documents": documents,
    }


def generate_answer(question: str) -> dict:
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

    retrieval = retrieve_context(question)
    documents = retrieval["documents"]

    context = "\n\n".join(documents)

    prompt = f"""
You are a helpful AI assistant answering questions using only the provided context.

If the answer is not in the context, say:
"I do not have enough information in the provided context to answer that."

Context:
{context}

Question:
{question}

Answer:
"""

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "Answer only from the provided context."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content

    return {
        "question": question,
        "answer": answer,
        "sources": documents,
    }

import chromadb
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

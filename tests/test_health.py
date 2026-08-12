from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ingest_sample_document():
    response = client.get("/ingest/sample")
    data = response.json()

    assert response.status_code == 200
    assert data["file"] == "data/sample_policy.txt"
    assert data["chunk_count"] > 0
    assert isinstance(data["chunks"], list)

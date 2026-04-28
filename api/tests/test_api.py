from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job():
    job_id = client.post("/jobs").json()["job_id"]
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200


def test_job_response_structure():
    job_id = client.post("/jobs").json()["job_id"]
    response = client.get(f"/jobs/{job_id}").json()

    assert "job_id" in response
    assert "status" in response

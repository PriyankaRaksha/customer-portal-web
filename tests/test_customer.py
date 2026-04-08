from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer():

    response = client.post("/customers")

    assert response.status_code == 200
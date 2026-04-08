from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_payment():

    response = client.post("/payment")

    assert response.status_code == 200
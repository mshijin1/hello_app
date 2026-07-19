from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greeting_endpoint_with_name():
    response = client.get("/api/greet?name=Agent")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello oye Agent"}

def test_greeting_endpoint_default():
    response = client.get("/api/greet")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello oye World"}
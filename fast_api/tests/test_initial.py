from starlette.testclient import TestClient
from app import app

# get and assign app to create test client
client = TestClient(app)

def test_read_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello from FastAPI Server!'}

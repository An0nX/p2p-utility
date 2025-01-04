import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_run_command():
    response = client.post("/cmd/", json={"command": "echo Hello"})
    assert response.status_code == 200
    assert "Hello" in response.json()["stdout"]

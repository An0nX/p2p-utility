"""Tests for the cmd router."""

import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_run_command():
    """Test that the cmd router can run a command and return the output."""
    response = client.post("/cmd/", json={"command": "echo Hello"})
    assert response.status_code == 200
    assert "Hello" in response.json()["stdout"]

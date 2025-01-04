"""Tests for filesystem router."""

import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_list_dir():
    """Test listing directories in the filesystem."""
    response = client.get("/fs/list?path=/")
    assert response.status_code == 200

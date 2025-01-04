import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_list_dir():
    response = client.get("/fs/list?path=/")
    assert response.status_code == 200

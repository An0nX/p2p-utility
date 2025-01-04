import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)
video_chunk = b"video_chunk"


@pytest.mark.asyncio
async def test_video_upload_and_return():
    response = client.post(
        "/stream/",
        content=video_chunk,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == video_chunk


@pytest.mark.asyncio
async def test_multiple_video_chunks():
    response = client.post(
        "/stream/",
        content=video_chunk * 3,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == video_chunk * 3


@pytest.mark.asyncio
async def test_empty_video_chunk():
    response = client.post(
        "/stream/",
        content=b"",
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == b""


@pytest.mark.asyncio
async def test_large_video_chunk():
    large_chunk = b"0" * (10**6)  # 1 МБ
    response = client.post(
        "/stream/",
        content=large_chunk,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == large_chunk

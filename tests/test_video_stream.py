"""Tests for video stream endpoint."""

import pytest
from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)
VIDEO_CHUNK = b"VIDEO_CHUNK"


@pytest.mark.asyncio
async def test_video_upload_and_return():
    """Test that video stream endpoint returns the same bytes as were sent."""
    response = client.post(
        "/stream/",
        content=VIDEO_CHUNK,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == VIDEO_CHUNK


@pytest.mark.asyncio
async def test_multiple_video_chunks():
    """Test that video stream endpoint can handle multiple chunks."""
    response = client.post(
        "/stream/",
        content=VIDEO_CHUNK * 3,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == VIDEO_CHUNK * 3


@pytest.mark.asyncio
async def test_empty_video_chunk():
    """Test that video stream endpoint returns empty bytes for empty request."""
    response = client.post(
        "/stream/",
        content=b"",
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == b""


@pytest.mark.asyncio
async def test_large_video_chunk():
    """Test that video stream endpoint can handle large chunks."""
    large_chunk = b"0" * (10**6)  # 1 МБ
    response = client.post(
        "/stream/",
        content=large_chunk,
        headers={"Content-Type": "application/octet-stream"},
    )

    assert response.status_code == 200

    assert response.content == large_chunk

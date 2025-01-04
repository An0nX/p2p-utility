"""
Module for handling video streaming from a request.

This module provides a single function, `video_stream_handler`, which takes a FastAPI
Request object and returns a StreamingResponse object containing the video data
streamed from the request.

The function handles errors occurring during the streaming process and raises an
HTTPException with a 500 status code in such cases.
"""

import io
from fastapi import HTTPException, Request
from fastapi.responses import StreamingResponse


async def video_stream_handler(request: Request):
    """
    Handle streaming of video data from a request.

    Args:
        request (Request): The request containing the video data to be streamed.

    Returns:
        StreamingResponse: A response object streaming the video data with 'video/mp4' media type.

    Raises:
        HTTPException: If an error occurs while processing the video data.
    """

    try:
        video_chunks = []

        async for chunk in request.stream():
            video_chunks.append(chunk)

        video_data = b"".join(video_chunks)

        return StreamingResponse(io.BytesIO(video_data), media_type="video/mp4")

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading video: {str(e)}"
        ) from e

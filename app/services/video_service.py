from fastapi import HTTPException, Request
from fastapi.responses import StreamingResponse
from io import BytesIO

async def video_stream_handler(request: Request):
    try:
        video_chunks = []

        async for chunk in request.stream():
            video_chunks.append(chunk)

        video_data = b"".join(video_chunks)

        return StreamingResponse(BytesIO(video_data), media_type="video/mp4")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading video: {str(e)}")

from fastapi import APIRouter, Request
from app.services.video_service import video_stream_handler

router = APIRouter()


@router.post("/")
async def stream_video(request: Request):
    """
    Stream video data.

    POST /stream/

    Request Body:
    - The video data to be streamed.

    Response:
    - The streamed video data.

    Raises:
    - HTTPException: If there is an error while streaming the video.
    """
    response = await video_stream_handler(request)
    return response

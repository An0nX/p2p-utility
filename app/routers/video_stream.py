from fastapi import APIRouter, Request
from app.services.video_service import video_stream_handler

router = APIRouter()


@router.post("/")
async def stream_video(request: Request):
    response = await video_stream_handler(request)
    return response

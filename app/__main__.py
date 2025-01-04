"""
Main application entry point for the P2P Utility.
This application provides APIs for command execution, filesystem access, and video streaming.
"""

from fastapi import FastAPI
import uvicorn
from app.routers import cmd, filesystem, video_stream
from app.config import Config

app = FastAPI(
    title=Config.APP_NAME, description=Config.DESCRIPTION, version=Config.VERSION
)

app.include_router(cmd.router, prefix="/cmd", tags=["Command Execution"])
app.include_router(filesystem.router, prefix="/fs", tags=["Filesystem"])
app.include_router(video_stream.router, prefix="/stream", tags=["Video Stream"])

if __name__ == "__main__":
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)


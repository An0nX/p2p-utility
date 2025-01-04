import os
import aiofiles
from fastapi.responses import FileResponse
from fastapi import HTTPException


def list_directory(path: str):
    if not os.path.isdir(path):
        raise HTTPException(status_code=404, detail="Directory not found")
    return os.listdir(path)


def download_file(path: str):
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path)


async def upload_file(path: str, file):
    destination = os.path.join(path, file.filename)
    async with aiofiles.open(destination, "wb") as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    return {"message": "File uploaded successfully"}


def delete_path(path: str):
    if os.path.isdir(path):
        os.rmdir(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        raise HTTPException(status_code=404, detail="Path not found")

"""
Module for providing file system operations.
"""

import os
import aiofiles
from fastapi.responses import FileResponse
from fastapi import HTTPException


def list_directory(path: str):
    """
    List files and directories in the given path.

    Args:
        path (str): The directory path to list.

    Returns:
        list: A list of files and directories in the specified path.

    Raises:
        HTTPException: If the directory is not found at the given path.
    """

    if not os.path.isdir(path):
        raise HTTPException(status_code=404, detail="Directory not found")
    return os.listdir(path)


def download_file(path: str):
    """
    Download a file from the given path.

    Args:
        path (str): The path to the file to be downloaded.

    Returns:
        FileResponse: The file response containing the requested file.

    Raises:
        HTTPException: If the file is not found at the given path.
    """

    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path)


async def upload_file(path: str, file):
    """
    Upload a file to the given path.

    Args:
        path (str): The directory path to upload the file to.
        file (UploadFile): The file to be uploaded.

    Returns:
        dict: A dictionary with a single key, "message", which contains a success message.

    Raises:
        HTTPException: If the file is not uploaded successfully.
    """
    destination = os.path.join(path, file.filename)
    async with aiofiles.open(destination, "wb") as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    return {"message": "File uploaded successfully"}


def delete_path(path: str):
    """
    Delete a file or directory from the given path.

    Args:
        path (str): The path to the file or directory to be deleted.

    Raises:
        HTTPException: If the file or directory is not found at the given path.
    """
    if os.path.isdir(path):
        os.rmdir(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        raise HTTPException(status_code=404, detail="Path not found")


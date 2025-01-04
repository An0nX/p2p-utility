"""
API Router for filesystem operations.

This module provides endpoints for listing, downloading, uploading, and deleting files and
directories.
"""

from fastapi import APIRouter, UploadFile, File
from app.services.fs_service import (
    list_directory,
    download_file,
    upload_file,
    delete_path,
)

router = APIRouter()


@router.get("/list")
async def list_dir(path: str = "/"):
    """
    List files and directories in the given path.

    Args:
        path (str): Directory path. Defaults to "/".

    Returns:
        dict: A dictionary with a single key, "files", which contains a list of files and
            directories.
    """
    return {"files": list_directory(path)}


@router.get("/download")
async def download(path: str):
    """
    Download a file from the given path.

    Args:
        path (str): The path to the file to be downloaded.

    Returns:
        FileResponse: The file response containing the requested file.

    Raises:
        HTTPException: If the file is not found at the given path.
    """
    return download_file(path)


@router.post("/upload")
async def upload(path: str, file: UploadFile = File(...)):
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
    return await upload_file(path, file)


@router.delete("/delete")
async def delete(path: str):
    """
    Delete a file or directory.

    Args:
        path (str): The path to the file or directory to be deleted.

    Returns:
        dict: A dictionary with a single key, "message", which contains a success message.

    Raises:
        HTTPException: If the file or directory is not found at the given path.
    """
    delete_path(path)
    return {"message": "Deleted successfully"}

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
    return {"files": list_directory(path)}


@router.get("/download")
async def download(path: str):
    return download_file(path)


@router.post("/upload")
async def upload(path: str, file: UploadFile = File(...)):
    return await upload_file(path, file)


@router.delete("/delete")
async def delete(path: str):
    delete_path(path)
    return {"message": "Deleted successfully"}

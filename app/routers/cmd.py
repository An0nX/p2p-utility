from fastapi import APIRouter, HTTPException
from app.services.cmd_service import execute_command

router = APIRouter()


@router.post("/")
async def run_command(data: dict):
    command = data.get("command")
    if not command:
        raise HTTPException(status_code=400, detail="No command provided")
    return await execute_command(command)


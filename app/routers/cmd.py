"""
API Router for command execution.

This module provides a single API endpoint for executing a system command.
"""

from fastapi import APIRouter, HTTPException
from app.services.cmd_service import execute_command

router = APIRouter()


@router.post("/")
async def run_command(data: dict):
    """
    Execute a system command.

    Args:
    - data (dict): Dictionary with a single key, "command", which is the command to execute.

    Returns:
    - dict: Dictionary with two keys, "stdout" and "stderr", each containing the respective
            output of the command.

    Raises:
    - HTTPException: If no command is provided.
    """
    command = data.get("command")
    if not command:
        raise HTTPException(status_code=400, detail="No command provided")
    return await execute_command(command)

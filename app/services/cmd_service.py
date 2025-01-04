import subprocess


async def execute_command(command: str):
    """
    Execute a system command.

    Args:
        command (str): The command to execute.

    Returns:
        dict: A dictionary with two keys, "stdout" and "stderr", each containing the respective
            output of the command.
    """
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = process.communicate()
    return {"stdout": stdout, "stderr": stderr}

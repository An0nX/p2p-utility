"""
Configuration class for the P2P Utility application.

This module contains a single class, `Config`, which provides
configuration values for the application. The values are loaded
from environment variables using the `python-dotenv` library.

The configuration values are:
- `APP_NAME`: The name of the application.
- `VERSION`: The version of the application.
- `DESCRIPTION`: A short description of the application.
- `HOST`: The host address to bind the application to.
- `PORT`: The port number to bind the application to.

"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME: str = os.getenv("APP_NAME", "P2P Utility")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    DESCRIPTION: str = os.getenv(
        "DESCRIPTION",
        "P2P utility for command execution, filesystem access, and video streaming"
    )
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))


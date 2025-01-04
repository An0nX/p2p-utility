from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "P2P Utility")
    VERSION = os.getenv("VERSION", "1.0.0")
    DESCRIPTION = os.getenv(
        "DESCRIPTION",
        "P2P utility for command execution, filesystem access, and video streaming"
    )
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

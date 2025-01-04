from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """
    Configuration class to store application settings from environment variables
    """

    APP_NAME: str = os.getenv("APP_NAME", "P2P Utility")
    """
    Name of the application

    Default: "P2P Utility"
    """

    VERSION: str = os.getenv("VERSION", "1.0.0")
    """
    Version of the application

    Default: "1.0.0"
    """

    DESCRIPTION: str = os.getenv(
        "DESCRIPTION",
        "P2P utility for command execution, filesystem access, and video streaming"
    )
    """
    Description of the application

    Default: "P2P utility for command execution, filesystem access, and video streaming"
    """

    HOST: str = os.getenv("HOST", "0.0.0.0")
    """
    Host of the application

    Default: "0.0.0.0"
    """

    PORT: int = int(os.getenv("PORT", 8000))
    """
    Port of the application

    Default: 8000
    """

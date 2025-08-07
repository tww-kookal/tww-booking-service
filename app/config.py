import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

class Settings:
    # App settings
    APP_NAME: str = "TWW Booking Service"
    VERSION: str = "1.0.0"

    # Google API credentials
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REFRESH_TOKEN: str = os.getenv("GOOGLE_REFRESH_TOKEN")
    GOOGLE_DRIVE_FOLDER_ID: str = os.getenv("GOOGLE_DRIVE_FOLDER_ID")

    # OAuth2 scopes
    GOOGLE_SCOPES: list = [
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.file",
    ]

    # Upload/Export paths
    TEMP_UPLOAD_DIR: str = "temp_uploads/"
    TEMP_PDF_DIR: str = "temp_pdfs/"

    # App behavior
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    # Host/port if needed
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()

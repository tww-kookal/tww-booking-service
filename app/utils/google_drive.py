import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Load credentials
SERVICE_ACCOUNT_FILE = 'credentials/service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
ROOT_FOLDER_ID = os.getenv("GOOGLE_DRIVE_ROOT_FOLDER_ID")  # Your base folder

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)


def create_booking_folder(booking_id: str) -> str:
    """Creates a folder inside ROOT_FOLDER_ID with name = booking_id"""
    folder_metadata = {
        'name': booking_id,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [ROOT_FOLDER_ID]
    }
    try:
        folder = drive_service.files().create(
            body=folder_metadata,
            fields='id'
        ).execute()
        return folder.get('id')
    except Exception as e:
        raise Exception(f"Failed to create folder: {str(e)}")


def upload_file_to_folder(file_path: str, file_name: str, folder_id: str) -> str:
    """Uploads a file to a specific Google Drive folder."""
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    try:
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        return file.get('webViewLink')  # Or return file.get('id')
    except Exception as e:
        raise Exception(f"Failed to upload file: {str(e)}")

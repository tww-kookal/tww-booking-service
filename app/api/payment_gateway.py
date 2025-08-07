# westwood_booking_apis.py

from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks, Request
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os

app = FastAPI()

# Placeholders for Google APIs and Payment Gateway
from utils.google_drive import create_booking_folder, upload_file_to_folder
from utils.google_sheets import insert_booking_record, update_payment_status, insert_feedback, get_home_availability
from utils.pdf_generator import generate_booking_pdf
from utils.notifications import send_whatsapp_message
from models.booking import BookingRequest

@app.post("/payment/webhook")
async def payment_webhook(request: Request):
    payload = await request.json()
    booking_id = verify_payment_webhook(payload)

    if booking_id:
        # Step 1: Update payment status in Google Sheet
        update_payment_status(booking_id, status="Confirmed")

        # Step 2: Generate PDF confirmation
        pdf_path = generate_booking_pdf(booking_id)
        folder_id = payload.get("folder_id")
        pdf_link = upload_file_to_folder(folder_id, pdf_path)

        # Step 3: Send confirmation via WhatsApp
        send_whatsapp_message(booking_id, pdf_link)

    return {"status": "success"}
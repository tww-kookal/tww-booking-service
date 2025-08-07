# westwood_booking_apis.py

from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks, Request
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from models.booking import BookingRequest
import os

app = FastAPI()

# Placeholders for Google APIs and Payment Gateway
from utils.google_drive import create_booking_folder, upload_file_to_folder
from utils.google_sheets import insert_booking_record, update_payment_status, insert_feedback, get_home_availability
from utils.pdf_generator import generate_booking_pdf

# ------------ API ROUTES ------------

@app.post("/book")
async def book_stay(
    request: Request,
    background_tasks: BackgroundTasks,
    booking: BookingRequest,
    id_proof: UploadFile = File(...)
):
    # Step 1: Create Drive folder
    folder_name = f"{booking.checkin_date}_{booking.room_name.replace(' ', '')}_{booking.name.replace(' ', '')}"
    folder_id = create_booking_folder(folder_name)

    # Step 2: Upload ID Proof
    id_proof_path = f"temp/{id_proof.filename}"
    with open(id_proof_path, "wb") as f:
        f.write(await id_proof.read())
    id_proof_link = upload_file_to_folder(folder_id, id_proof_path)

    # Step 3: Insert into Google Sheet
    booking_id = insert_booking_record(booking.dict(), folder_id, id_proof_link)

    # Step 4: Generate UPI Payment Link
    #upi_link = create_upi_payment_link(booking_id, booking.name)

    return {"booking_id": booking_id, "payment_link": "upi_link"}

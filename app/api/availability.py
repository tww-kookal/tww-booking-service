# westwood_booking_apis.py

from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks, Request
from pydantic import BaseModel
from typing import List, Optional
from models.availability import AvailabilityRequest
from datetime import datetime
import os

app = FastAPI()

# Placeholders for Google APIs and Payment Gateway
from ..utils.google_sheets import insert_booking_record, update_payment_status, insert_feedback, get_home_availability

# ------------ API ROUTES ------------

@app.post("/availability")
async def check_availability(query: AvailabilityRequest):
    available_homes = get_home_availability(
        checkin_date=query.checkin_date,
        checkout_date=query.checkout_date,
        number_of_people=query.number_of_people
    )
    return {"available_homes": available_homes}

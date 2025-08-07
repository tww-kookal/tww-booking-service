# westwood_booking_apis.py

from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks, Request
from pydantic import BaseModel
from typing import List, Optional
from models.feedback import FeedbackRequest
from datetime import datetime
import os

app = FastAPI()

# Placeholders for Google APIs and Payment Gateway
from utils.google_sheets import insert_booking_record, update_payment_status, insert_feedback, get_home_availability

# ------------ API ROUTES ------------

@app.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    insert_feedback(feedback.dict())
    return {"status": "feedback received"}


@app.post("/feedback/reminder")
async def feedback_reminder():
    # This would be called by a CronJob
    # from utils.scheduler import check_pending_feedbacks
    # check_pending_feedbacks()
    return {"status": "reminders sent"}



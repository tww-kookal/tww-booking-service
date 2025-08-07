from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ------------ MODELS ------------
class BookingRequest(BaseModel):
    name: str
    room_name: str
    checkin_date: str  # YYYY-MM-DD
    checkout_date: str
    number_of_people: int
    amenities: List[str]
    contact_number: str

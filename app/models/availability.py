from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AvailabilityRequest(BaseModel):
    checkin_date: str #YYYY-MM-DD
    checkout_date: str #YYYY-MM-DD
    number_of_people: int

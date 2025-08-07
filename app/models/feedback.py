from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FeedbackRequest(BaseModel):
    booking_id: str
    rating: int
    comments: Optional[str] = ""


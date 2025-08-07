from fastapi import FastAPI
from app.api import booking, availability, feedback, payment_gateway

app = FastAPI()

# Register routers
app.include_router(booking.router, prefix="/booking")
app.include_router(availability.router, prefix="/availability")
app.include_router(payment_gateway.router, prefix="/payment")
app.include_router(feedback.router, prefix="/feedback")

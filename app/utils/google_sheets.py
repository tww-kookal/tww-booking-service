# utils/google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import uuid

creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
gc = gspread.authorize(creds)

sheet = gc.open_by_key(SHEET_ID)


def insert_booking_record(data: dict, folder_id: str, id_proof_link: str) -> str:
    booking_id = str(uuid.uuid4())[:8]
    ws = sheet.worksheet(BOOKING_SHEET)
    ws.append_row([
        booking_id,
        data['name'],
        data['room_name'],
        data['checkin_date'],
        data['checkout_date'],
        data['number_of_people'],
        ", ".join(data['amenities']),
        str(data['demographic_details']),
        folder_id,
        id_proof_link,
        "Pending",
        "Not Confirmed",
        ""
    ])
    return booking_id


def update_payment_status(booking_id: str, status: str):
    ws = sheet.worksheet(BOOKING_SHEET)
    records = ws.get_all_records()
    for idx, row in enumerate(records, start=2):
        if row['booking_id'] == booking_id:
            ws.update_cell(idx, 12, status)  # Payment Status
            return


def insert_feedback(feedback: dict):
    ws = sheet.worksheet(FEEDBACK_SHEET)
    ws.append_row([
        feedback['booking_id'],
        feedback['rating'],
        feedback['comments'],
        datetime.now().isoformat(),
        "No",
        "No"
    ])


def get_home_availability(checkin_date: str, checkout_date: str, number_of_people: int) -> list:
    ws = sheet.worksheet(BOOKING_SHEET)
    bookings = ws.get_all_records()
    occupied = {}

    for row in bookings:
        if row['payment_status'] != 'Confirmed':
            continue
        existing_start = datetime.strptime(row['checkin_date'], "%Y-%m-%d")
        existing_end = datetime.strptime(row['checkout_date'], "%Y-%m-%d")
        requested_start = datetime.strptime(checkin_date, "%Y-%m-%d")
        requested_end = datetime.strptime(checkout_date, "%Y-%m-%d")

        # Check if the dates overlap
        if requested_start <= existing_end and existing_start <= requested_end:
            occupied[row['room_name']] = occupied.get(row['room_name'], 0) + row['number_of_people']

    # Find available homes
    required_people = number_of_people
    available_homes = []

    for home, capacity in HOMES_INFO.items():
        booked = occupied.get(home, 0)
        available_capacity = capacity - booked
        if available_capacity > 0:
            used = min(available_capacity, required_people)
            available_homes.append({"home": home, "capacity": used})
            required_people -= used
        if required_people <= 0:
            break

    return available_homes if required_people <= 0 else []

import pdfkit
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_booking_confirmation_pdf(booking_details, file_path):
    """
    Generates a booking confirmation PDF with the provided booking details.

    :param booking_details: Dictionary with booking information.
    :param file_path: Path to save the PDF file.
    """
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 14)
    c.drawString(100, height - 50, "Booking Confirmation")

    c.setFont("Helvetica", 12)
    y_position = height - 100

    for key, value in booking_details.items():
        c.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20

    c.save()

    return file_path


# Example usage
if __name__ == "__main__":
    booking = {
        "Guest Name": "John Doe",
        "Room Name": "Cottage 1",
        "Check-In": "2025-08-10",
        "Check-Out": "2025-08-12",
        "Number of People": 3,
        "Payment Status": "Confirmed",
    }
    output_path = os.path.join("./", "booking_confirmation.pdf")
    generate_booking_confirmation_pdf(booking, output_path)

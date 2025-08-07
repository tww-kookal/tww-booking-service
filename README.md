# 🏡 TWW Booking Service
A Python-based microservice for managing homestay bookings, integrated with Google Drive, Google Sheets, WhatsApp notifications, UPI payment simulation, PDF generation, and feedback collection.

A modular, scalable microservice for managing bookings of vacation homes with Google Sheets, Google Drive, WhatsApp notifications, PDF generation, payment simulation, and containerization support.

---

## 📁 Project Structure

```bash
tww-booking-service/
├── app.py                         # Main FastAPI entrypoint
├── config.py                      # App configuration loader
├── requirements.txt               # Project dependencies
├── Dockerfile                     # Docker container definition
├── README.md                      # Project overview and usage
├── credentials/
│   └── service_account.json       # Google API credentials
├── utils/
│   ├── google_drive.py            # Google Drive folder creation and file upload
│   ├── google_sheets.py           # Sheet operations: booking, payment, feedback, availability
│   ├── pdf_generator.py           # Booking confirmation PDF generation
│   ├── payment_gateway.py         # UPI payment simulation
│   ├── notifications.py           # WhatsApp notifications
│   ├── scheduler.py               # Feedback reminder scheduler
└── static/
    └── confirmation_template.html # HTML template for PDF booking confirmations
```
---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud project with Sheets and Drive API enabled
- Twilio (or mock) for WhatsApp messaging
- wkhtmltopdf (for PDF generation using `pdfkit`)
- Docker (for containerized deployment)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-org/tww-booking-service.git
cd tww-booking-service
````

2. Set up a Python environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Provide credentials:

* Place your Google service account key file in `credentials/service_account.json`.
* Add necessary config values in `config.py`.

4. Run the service:

```bash
uvicorn app.main:app --reload
```

---

## 🧠 API Overview

### `/api/bookings/create`

* **POST**
* Create a booking entry with details like guest name, number of people, dates, etc.
* Generates:

  * Google Sheet row
  * PDF confirmation
  * Google Drive folder with uploaded files
  * WhatsApp confirmation
  * UPI payment link

### `/api/bookings/payment`

* **POST**
* Mock endpoint for payment status update using webhook or manual update.

### `/api/bookings/feedback`

* **POST**
* Collect feedback post-stay. Scheduled reminders handled by a cron job in `scheduler.py`.

### `/api/availability/check`

* **GET**
* Checks room/home availability based on date and guest count.
* Suggests multiple homes if group size exceeds one home.

---

## 💡 Feature Breakdown

| Feature                   | File                       | Description                                         |
| ------------------------- | -------------------------- | --------------------------------------------------- |
| Google Sheets Integration | `utils/google_sheets.py`   | CRUD for bookings, payments, feedback, availability |
| Google Drive Uploads      | `utils/google_drive.py`    | Create booking-specific folders, upload files       |
| PDF Confirmation          | `utils/pdf_generator.py`   | Generate booking summary PDFs                       |
| WhatsApp Notification     | `utils/notifications.py`   | Message confirmations & reminders                   |
| Simulated Payments        | `utils/payment_gateway.py` | Generate mock UPI links & callbacks                 |
| Feedback Reminders        | `utils/scheduler.py`       | Remind users post-stay using scheduler/cron         |
| Containerization          | `Dockerfile`               | Run the app in isolated Docker container            |
| Config Management         | `config.py`                | Centralized config for external service links       |

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t tww-booking-service .
```

### Run Docker Container

```bash
docker run -d -p 8000:8000 --name tww-booking-service tww-booking-service
```

### Access the API

```bash
http://localhost:8000/docs
```

---

## 📦 Dependencies

* `fastapi` – Web framework
* `uvicorn` – ASGI server
* `google-api-python-client`, `gspread`, `oauth2client` – Google Sheets & Drive
* `pdfkit`, `reportlab` – PDF generation
* `twilio` – WhatsApp Messaging
* `apscheduler` – Scheduled feedback reminders
* `python-dotenv` – Environment variables

---

## 🔐 Security Note

* Do **not** commit `credentials/service_account.json` to version control.
* Secure your webhook endpoints.
* Consider using Vault/Secrets Manager in production.
* Sanitize all user inputs before sending to external services.

---

## 🛠 Future Enhancements

* Integrate real payment gateway (like Razorpay/PayPal)
* Add admin dashboard for managing bookings
* Multi-lingual WhatsApp template support
* Use OAuth 2.0 flow for secure Google access
* Logging and alerting (Sentry, ELK)

---

## 👤 Author

**Pranavam Siddharthan**
[LinkedIn](https://www.linkedin.com/in/pranavam-siddharthan)
[GitHub](https://github.com/pranavamsiddharthan)

---

## 📜 License

This project is licensed under the MIT License.

```

---

Let me know if you'd like this saved as a downloadable `README.md` file or published to a GitHub repo directly.
```


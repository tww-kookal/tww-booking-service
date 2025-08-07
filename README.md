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

### 🧩 Dependencies

This project depends on the following Python packages (from `requirements.txt`):

* `annotated-types==0.7.0`
* `anyio==4.10.0`
* `cachetools==5.5.2`
* `certifi==2025.8.3`
* `charset-normalizer==3.4.2`
* `click==8.2.1`
* `colorama==0.4.6`
* `fastapi==0.116.1` – Web framework for building APIs
* `google-api-core==2.25.1`
* `google-api-python-client==2.178.0` – Google APIs Python client
* `google-auth==2.40.3`
* `google-auth-httplib2==0.2.0`
* `google-auth-oauthlib==1.2.2`
* `googleapis-common-protos==1.70.0`
* `gspread==6.2.1` – Google Sheets API wrapper
* `h11==0.16.0`
* `httplib2==0.22.0`
* `idna==3.10`
* `oauth2client==4.1.3`
* `oauthlib==3.3.1`
* `pdfkit==1.0.0` – Convert HTML to PDF
* `pillow==11.3.0` – Python Imaging Library
* `proto-plus==1.26.1`
* `protobuf==6.31.1`
* `pyasn1==0.6.1`
* `pyasn1_modules==0.4.2`
* `pydantic==2.11.7` – Data validation
* `pydantic_core==2.33.2`
* `pyparsing==3.2.3`
* `python-dotenv==1.1.1` – Load environment variables
* `reportlab==4.4.3` – PDF generation library
* `requests==2.32.4` – HTTP library
* `requests-oauthlib==2.0.0`
* `rsa==4.9.1`
* `six==1.17.0`
* `sniffio==1.3.1`
* `starlette==0.47.2` – ASGI toolkit (used with FastAPI)
* `typing-inspection==0.4.1`
* `typing_extensions==4.14.1`
* `uritemplate==4.2.0`
* `urllib3==2.5.0`
* `uvicorn==0.35.0` – ASGI server for running FastAPI apps

To install all dependencies, run:

```bash
pip install -r requirements.txt
```
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

---
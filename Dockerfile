# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

# Set working directory
WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port your app runs on (e.g., 8000)
EXPOSE 8000

# Start the service (using uvicorn if FastAPI or gunicorn/flask for Flask)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

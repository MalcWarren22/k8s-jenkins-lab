# Simple Python Flask app
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

EXPOSE 8000

# Use gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

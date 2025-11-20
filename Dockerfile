

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app
COPY tests/ ./tests

# Expose port and run
EXPOSE 5000

# Run the application
CMD ["python", "app/app.py"]

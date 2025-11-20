
# Use an official Python runtime as a parent image
FROM Python:3.11-slim

# Set working dir
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./

# Expose port and run
EXPOSE 5000
CMD ["Python","app.py"]


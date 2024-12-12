# Use an official Python image as the base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y netcat-openbsd && apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# Add an entrypoint script to wait for database to be ready
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run entrypoint script followed by Django server
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "hyper_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

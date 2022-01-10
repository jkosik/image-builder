FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
COPY reboot-ec2.py .
RUN pip install -r requirements.txt

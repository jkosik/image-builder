FROM python:3.9-slim

WORKDIR /app
COPY aws/requirements.txt .
COPY aws/reboot-ec2.py .
RUN pip install -r requirements.txt


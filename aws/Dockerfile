FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
COPY reboot-ec2.py .
RUN pip install awscli==1.22.32 boto3==1.20.32
#RUN pip install -r /app/requirements.txt

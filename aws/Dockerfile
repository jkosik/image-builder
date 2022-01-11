FROM python:3.9-slim

RUN apt update && apt-get upgrade -y && apt install -y \
    procps \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY aws/requirements.txt .
COPY aws/reboot-ec2.py .
RUN pip install -r requirements.txt


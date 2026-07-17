FROM python:3.11-slim@sha256:4e8e2c6b2b5c5b9f3d6f6d5e6a9f4d8c3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log

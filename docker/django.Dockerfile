FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update && \
  apt-get install -y \
	  build-essential \
	  libpq-dev \
	  libffi-dev \
	  pkg-config \
	  netcat-openbsd \
	  postgresql-client && \
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

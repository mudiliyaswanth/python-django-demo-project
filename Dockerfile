FROM python:3.13.11-slim 

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update \
&& apt-get install -y gcc libpq-dev \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
    
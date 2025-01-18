FROM python:3.10-slim

RUN mkdir /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

RUN chmod +x /app/entrypoint.sh
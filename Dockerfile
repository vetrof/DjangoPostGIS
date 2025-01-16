FROM python:3.10-slim

WORKDIR /code

COPY . /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
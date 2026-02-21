FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend

COPY . /backend

EXPOSE 5001
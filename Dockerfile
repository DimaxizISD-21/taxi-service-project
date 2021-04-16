FROM python:3.9
MAINTAINER Nikolaenko Oleksiy

ENV PYTHONUNBUFFERED 1

COPY ./taxi_service/requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /taxi_service
WORKDIR /taxi_service
COPY ./taxi_service /taxi_service

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

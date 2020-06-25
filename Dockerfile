FROM alpine:latest

ADD . /

RUN apk add py3-flask-sqlalchemy py3-flask py3-mysqlclient

EXPOSE 5000

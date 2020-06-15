FROM alpine:latest

ADD . /

RUN apk add python3 py-pip --no-cache

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD python3 app.py

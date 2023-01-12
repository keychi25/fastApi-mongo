FROM python:3.7-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN apk add --update --no-cache make bash gcc g++ tzdata git\
  && pip install --upgrade pip \
  && pip install uvicorn==0.11.8 \
  && pip install debugpy

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app/.pip

ADD docker/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

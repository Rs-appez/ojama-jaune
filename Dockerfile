
FROM python:3.13-rc-alpine

ENV TZ="Europe/Brussels"

RUN apk update \
    && apk add ffmpeg

WORKDIR /ojama_jaune


COPY requirements.txt /ojama_jaune/
RUN pip install -r requirements.txt
COPY . /ojama_jaune/
CMD python main.py

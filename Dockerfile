FROM python:3.14.0a1-slim

ENV TZ="Europe/Brussels"

RUN apt-get update \
    && apt-get install -y ffmpeg

WORKDIR /ojama_jaune


COPY requirements.txt /ojama_jaune/
RUN pip install -r requirements.txt
COPY . /ojama_jaune/
CMD python main.py

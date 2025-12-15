FROM python:3.13-alpine

ENV TZ="Europe/Brussels"
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache ffmpeg

WORKDIR /ojama_jaune
COPY requirements.txt /ojama_jaune/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /ojama_jaune/

CMD ["python3", "main.py"]

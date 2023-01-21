
FROM python:3.10

RUN apt-get update \
    && apt-get install -y ffmpeg

WORKDIR /ojama_jaune

EXPOSE 8080
EXPOSE 53
EXPOSE 22

COPY requirements.txt /ojama_jaune/
RUN pip install -r requirements.txt
COPY . /ojama_jaune/
CMD python main.py
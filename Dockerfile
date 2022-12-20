
FROM python:3.10
WORKDIR /ojama_jaune
EXPOSE 80
EXPOSE 443
EXPOSE 8080

COPY requirements.txt /ojama_jaune/
RUN pip install -r requirements.txt
COPY . /ojama_jaune/
RUN apk add ffmpeg
CMD python main.py
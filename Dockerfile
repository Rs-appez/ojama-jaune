FROM python:3.10
WORKDIR /ojama_jaune
COPY requirements.txt /ojama_jaune/
RUN pip install -r requirements.txt
COPY . /ojama_jaune/
CMD python main.py
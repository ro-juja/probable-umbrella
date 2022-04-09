FROM python:3.7-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
COPY models/clean_model.csv clean_model.csv

RUN pip3 install -r requirements.txt

COPY . . 

CMD [ "python3", "models/final_model.py"]


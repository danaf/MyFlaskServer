# syntax=docker/dockerfile:1

FROM python:3.12.1

WORKDIR /mypython-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=hello.py

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD [ "python3", "-m" , "flask", "run", "--host=::", "--port=5000"]

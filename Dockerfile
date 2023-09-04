# syntax=docker/dockerfile:1

# docker build -t flask-docker .
# docker run -d -p 5000:5000 -v /home/studpufffin/PycharmProjects/flaskPredict/app:/python-docker/app flask-docker

FROM python:3.8-slim-buster

WORKDIR /python-docker

ENV FLASK_APP=app \
FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "/python-docker/app/entrypoint.sh"]

ENTRYPOINT ["app/entrypoint.sh"]
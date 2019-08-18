FROM python:latest
ENV LANG C.UTF-8

RUN mkdir /django

RUN rm -f /etc/apt/sources.list
COPY ./config/sources.list /etc/apt/sources.list
RUN apt-get update && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./requirements.txt /django/requirements.txt
RUN pip install -r /django/requirements.txt
RUN apt-get -y update && apt-get -y autoremove

WORKDIR /django

EXPOSE 8100

CMD gunicorn -b :8100 django.wsgi
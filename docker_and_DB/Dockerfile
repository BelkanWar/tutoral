FROM python:3.12.4-slim-bookworm AS base
WORKDIR /workplace

ENV PYROOT=/pyroot
ENV PYTHONUSERBASE=$PYROOT

FROM base AS builder

RUN apt update  && \
    apt install -y apt-utils \
                   build-essential \
                   procps \
                   htop \
                   wget \
                   vim \
                   mysql-server \
                   mysql-client \
                   libmysqlclient-dev \ 
                   phpmyadmin && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile

COPY docker_and_DB ./

CMD  ["/bin/sh", "-ec", "sleep infinity"]
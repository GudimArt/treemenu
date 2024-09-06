FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc

COPY pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && poetry install --no-root --no-ansi

COPY . /app

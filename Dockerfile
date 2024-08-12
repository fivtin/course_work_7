FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

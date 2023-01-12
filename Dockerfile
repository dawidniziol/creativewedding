FROM python:3.9.7-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#standard
RUN apt-get update && apt-get install python-dev git curl libpq-dev -y
RUN pip install --upgrade pip
RUN pip install poetry

#working directory
WORKDIR /app/

RUN poetry config virtualenvs.path /venv

#new user
RUN addgroup app --gid 1000 && \
    useradd app --uid 1000 --gid app --home-dir /app/ && \
    chown -R app:app /app

USER app

#copy poetry file and instal
COPY pyproject.toml poetry.lock /app/

RUN poetry install

#copy project
COPY . .
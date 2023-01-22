FROM python:3.10-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN poetry install
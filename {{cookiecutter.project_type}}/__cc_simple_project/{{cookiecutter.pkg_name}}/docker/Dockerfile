FROM python:3.10.8-slim

# Metadata
LABEL name={{cookiecutter.project}}
LABEL maintainer={{cookiecutter.author}}

# Install poetry
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y curl

ARG POETRY_VERSION=1.5.0
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

# Set working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install --only main --no-interaction --no-ansi

# Copy all files
COPY settings ./settings
COPY docker/start.sh .
COPY main.py .
# TODO add other relevant files

RUN chmod a+x start.sh

CMD ./start.sh

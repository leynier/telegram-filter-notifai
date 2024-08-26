FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN apt update && apt install -y gcc make libffi-dev libssl-dev sqlite3

ADD . /app
WORKDIR /app

RUN mkdir -p data sessions

RUN make install

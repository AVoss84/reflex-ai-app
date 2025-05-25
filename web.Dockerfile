FROM python:3.12 AS builder

WORKDIR /app

# Install unzip and curl
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

COPY assets/ /app/assets
COPY web_app/ /app/web_app
#COPY .web/ /app/.web/
COPY pyproject.toml /app/pyproject.toml
COPY rxconfig.py /app/rxconfig.py

RUN pip install uv
RUN uv venv --python 3.12 && uv sync --no-cache
# exports the frontend assets to the .web/_static directory
RUN .venv/bin/reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# https://reflex.dev/blog/2024-10-8-self-hosting-reflex-with-docker/
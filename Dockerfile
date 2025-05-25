FROM python:3.12-slim
#EXPOSE 8000
WORKDIR /app

# # Install unzip and curl
# RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

COPY assets/ /app/assets
COPY web_app/ /app/web_app
# COPY .web/ /app/.web/
COPY pyproject.toml /app/pyproject.toml
COPY rxconfig.py /app/rxconfig.py

RUN pip install uv
RUN uv venv --python 3.12 && uv sync --no-cache
## Export static copy of frontend to /app/.web/_static
#RUN reflex export --frontend-only --no-zip
#RUN .venv/bin/reflex init --template blank

CMD [ "/bin/bash", "-c", "source .venv/bin/activate && reflex run --backend-only --loglevel debug" ]
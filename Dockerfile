FROM python:3.12-slim
EXPOSE 8080 8000
WORKDIR /app
COPY assets/ /app/assets
COPY web_app/ /app/web_app
COPY .web/ /app/.web/
COPY pyproject.toml /app/pyproject.toml

RUN pip install uv
RUN uv venv --python 3.12 && uv sync --no-cache
CMD [ "/bin/bash", "-c", "source .venv/bin/activate && reflex run --frontend-port 8080 --backend-port 8000"]
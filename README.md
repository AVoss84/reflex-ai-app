# Chat assistant Web App

A simple chat assistant web application built with [Reflex](https://reflex.dev/). It uses Gemini 2.5 Flash under the hood to answer user questions. For deployment, [see blog](https://reflex.dev/blog/2024-10-8-self-hosting-reflex-with-docker/).

## Features

- Chat interface with question and answer display
- Clear chat history functionality
- Responsive UI with custom styling

## Project Structure

```
├── assets
├── Dockerfile
├── Makefile
├── pyproject.toml
├── README.md
├── rxconfig.py
└── web_app
    ├── backend.py
    ├── state.py
    ├── style.py
    └── web_app.py
```

## Package installation and application develoment

Create virtual environment: 
```bash
uv venv --python 3.12
uv sync
source .venv/bin/activate
```

Start app locally:
```bash
make ui       
```

Run formating: 
```bash
make format
```
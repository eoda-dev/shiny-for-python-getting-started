# Shiny for Python Getting Started

## Start from scratch

Create a Python Shiny environment:

```bash
uv init [-p 3.9]
uv add shiny

source .venv/bin/activate

shiny --version

shiny --help

shiny create --help
```

Create a new Shiny Express app from template:

```bash
shiny create -d basic_app -t basic-app -m express

shiny run basic_app/app.py
```

## Templates

* [posit-dev/py-shiny-templates](https://github.com/posit-dev/py-shiny-templates)

## Deployment

To run Shiny apps in production you should use `gunicorn` or `uvicorn`:

```bash
uv add gunicorn

shiny create -d basic_app_core -t basic-app -m core

gunicorn basic_app_core.app:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Examples

* [basic_app](basic_app)
* [basic_app_core](basic_app_core)
* [routes_example_app](routes_example_app)
* [shinylive_quarto](shinylive_quarto)
* [shinylive_without_quarto](shinylive_without_quarto)

## Docker

```bash
docker pull ghcr.io/eoda-dev/shinylive-nginx:latest

docker run --rm -p 8085:80 ghcr.io/eoda-dev/shinylive-nginx:latest
```
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

## Use templates from GitHub

* [eoda-dev/py-shiny-templates](https://github.com/eoda-dev/py-shiny-templates)
* [posit-dev/py-shiny-templates](https://github.com/posit-dev/py-shiny-templates)

```bash
shiny create -g eoda-dev/py-shiny-templates -t fastapi-routes

shiny create -g posit-dev/py-shiny-templates -t map-distance
```

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

## Docker Image Releases

### Shinylive inside nginx

```bash
docker pull ghcr.io/eoda-dev/shinylive-nginx:latest

docker run --rm -p 8085:80 ghcr.io/eoda-dev/shinylive-nginx:latest
```

Navigate to [http://localhost:8085/shinylive-app/](http://localhost:8085/shinylive-app/)

### Shiny and FastAPI in one app

```bash
docker pull ghcr.io/eoda-dev/shiny-meets-fastapi:latest

docker run -p 3333:3333 --rm ghcr.io/eoda-dev/shiny-meets-fastapi:latest
```

Navigate to:

* Shiny app: [http://localhost:3333](http://localhost:3333)
* FastAPI REST API docs: [http://localhost:3333/api/docs](http://localhost:3333/api/docs)

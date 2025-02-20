# Routes Example App

Run app:

```bash
uv sync

# source .venv/bin/activate

gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

Build and run Docker image:

```bash
docker build -t shiny-for-py/routes-app:1.0.0 .

docker run --rm -p 3333:3333 shiny-for-py/routes-app:1.0.0
```

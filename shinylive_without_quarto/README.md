# Shinylive without quarto

Run app:

```bash
uv sync

uvicorn --reload app:app
```

Create standalone Shinylive app in `site` folder:

```bash
shinylive export . site
```

Start local webserver to server the app:

```bash
python3 -m http.server --directory site --bind localhost 8008
```

Navigate to [http://localhost:8008](http://localhost:8008)

Build Docker image to server site with Nginx:

```bash
docker build -t shiny-for-py/shinylive-app-nginx:1.0.0 .

docker run -p 8085:80 --rm shiny-for-py/shinylive-app-nginx:1.0.0
```

Navigate to [http://localhost:8085/shinylive-app/](http://localhost:8085/shinylive-app/)

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

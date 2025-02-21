# Shinylive Quarto

```bash
# pip install uv
uv sync

quarto add --no-prompt quarto-ext/shinylive

quarto render index.qmd

python -m http.server
```

Navigate to [http://localhost:8000](http://localhost:8000).

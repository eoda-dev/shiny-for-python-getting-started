# Shinylive Quarto

```bash
# pip install uv
uv sync

quarto add quarto-ext/shinylive

quarto render basic_app.qmd

python -m http.server
```
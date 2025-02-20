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

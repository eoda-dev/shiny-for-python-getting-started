from fastapi import FastAPI
from shiny import App, ui
from starlette.applications import Starlette
from starlette.routing import Mount

# ---
app_fastapi = FastAPI()


@app_fastapi.get("/")
def index():
    return dict(name="my-awesome-api", version="1.0.0")


# ---
app_shiny = App(ui.page_fluid("hello from shiny!"), None)

# ---
routes = [Mount("/api", app=app_fastapi), Mount("/", app=app_shiny)]

app = Starlette(routes=routes)

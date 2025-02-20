FROM python:3.11

RUN pip install uv

COPY ./ opt/shiny

WORKDIR /opt/shiny

RUN uv sync

EXPOSE 3333

CMD [".venv/bin/gunicorn", "app:app", "-w 4", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:3333"]


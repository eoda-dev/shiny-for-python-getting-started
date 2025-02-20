FROM python:3.11 AS builder

RUN pip install uv

COPY ./ /opt/shinylive

WORKDIR /opt/shinylive

RUN uv sync

RUN .venv/bin/shinylive export . shinylive-app

# ---
FROM nginx:latest

COPY --from=builder /opt/shinylive /usr/share/nginx/html

# COPY --from=builder /opt/shinylive/shinylive-app /usr/share/nginx/html

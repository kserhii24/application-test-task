# Use Python slim image for building dependencies
FROM python:3.11-slim AS builder-image

WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    python -m venv /app/venv

ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt


FROM python:3.11-slim AS runner-image

RUN userdel www-data && \
		useradd --home-dir /app --create-home www-data 

COPY --from=builder-image /app/venv /app/venv

USER www-data

WORKDIR /app
COPY --chown=www-data:www-data . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/app/venv

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["hypercorn", "--bind", "0.0.0.0:5000", "app:app"]

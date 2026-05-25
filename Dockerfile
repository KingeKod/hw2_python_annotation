FROM python:3.15.0b1-slim

WORKDIR /app

# Установка ca-certificates и gcc (для компиляции нативных зависимостей mypy)
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates gcc libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка uv из официального образа (без curl, без SSL-проблем)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY --from=ghcr.io/astral-sh/uv:latest /uvx /usr/local/bin/uvx

# Копирование файлов конфигурации проекта
COPY pyproject.toml uv.lock ./

# Установка зависимостей
RUN uv sync --frozen --dev

# Копирование проекта
COPY src/ ./src/
COPY main.py ./main.py
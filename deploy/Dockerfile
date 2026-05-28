# syntax=docker/dockerfile:1.9@sha256:fe40cf4e92cd0c467be2cfc30657a680ae2398318afd50b0c80585784c604f28
FROM ghcr.io/astral-sh/uv:0.11.15@sha256:e590846f4776907b254ac0f44b5b380347af5d90d668138ca7938d1b0c2f98d3 AS uv

FROM python:3.14.5@sha256:89a288a9a9e9141b9f0c51744c358138da6369897792f1af3f5425e407d9529a AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_CACHE=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY src ./src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-editable

FROM python:3.14.5@sha256:89a288a9a9e9141b9f0c51744c358138da6369897792f1af3f5425e407d9529a AS runtime

ARG IMAGE_VERSION=dev

LABEL org.opencontainers.image.title="notebooklm-mcp-agent" \
      org.opencontainers.image.description="MCP server and CLI for NotebookLM workflows" \
      org.opencontainers.image.source="https://github.com/oaslananka/notebooklm-mcp-agent" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.version="${IMAGE_VERSION}"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    NOTEBOOKLM_MCP_TRANSPORT=http \
    NOTEBOOKLM_MCP_HTTP_HOST=0.0.0.0 \
    NOTEBOOKLM_MCP_HTTP_PORT=8080 \
    NOTEBOOKLM_MCP_LOG_FORMAT=json

RUN useradd --create-home --uid 10001 --shell /bin/sh appuser \
    && mkdir -p /home/appuser/.local/share/notebooklm-agent /home/appuser/.config/notebooklm-agent \
    && chown -R appuser:appuser /home/appuser

WORKDIR /app
COPY --from=builder --chown=appuser:appuser /app/.venv ./.venv

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz', timeout=3)"

CMD ["notebooklm-agent", "serve", "--host", "0.0.0.0", "--port", "8080", "--auth", "bearer"]

# ---- Build Stage ----
FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.7.12 /uv /uvx /bin/

WORKDIR /project

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

COPY . .
RUN uv sync --frozen --no-dev

# ---- Runtime Stage ----
FROM python:3.13-slim AS runtime

WORKDIR /project

COPY --from=builder /project/.venv /project/.venv
COPY --from=builder /project /project

ENV PATH="/project/.venv/bin:$PATH"
ENV PYTHONPATH="/project"

CMD ["python", "app/main.py", "-launch_bot", "--name=Test"]
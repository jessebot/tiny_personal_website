# ---------------------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------------------

FROM python:3.12-alpine AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock README.md tiny_personal_website /app/

RUN apk add build-base libffi-dev && \
    pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-ansi --no-root

# ---------------------------------------------------------------------------------------
# DEPLOY
# ---------------------------------------------------------------------------------------

FROM python:3.12-alpine as deploy

ENV CONFIG_FILE="/app/tiny_personal_website/config/config.yaml"

WORKDIR /app

# copy the already built package
COPY --from=builder /app /app
COPY . /app

# Create a new group `app` with Group ID `1000`.
# Create a new user `app`, sets home directory to `/app`, User ID `1000`, in
# the group `app`. The `-DH` option results in a system account.
RUN addgroup --gid 1000 app && \
    adduser app -h /app -u 1000 -G app -DH

# Change the user for subsequent commands in Dockerfile to the user with ID
# `1000`.
USER 1000

# CMD ["/app/.venv/bin/gunicorn", "--bind", ":80", "app:app"]
CMD ["/app/.venv/bin/gunicorn"  , "-b", "0.0.0.0:8080", "app:app"]

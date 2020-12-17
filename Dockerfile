# ======================================================================
FROM python:3.9-slim AS app-base
# ======================================================================
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN groupadd -g 1000 appuser \
    && useradd -u 1000 -g appuser -ms /bin/bash appuser \
    && chown -R appuser:appuser /app

COPY --chown=appuser:appuser docker-entrypoint.sh requirements.txt /app/

RUN apt-get update \
    && apt-get -y install sqlite3 libsqlite3-dev \
    && pip install -U --ignore-installed --no-cache-dir requests \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives

COPY --chown=appuser:appuser docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

# ============================
FROM app-base AS development
# ============================
COPY --chown=appuser:appuser . /app/

USER appuser
EXPOSE 8001/tcp

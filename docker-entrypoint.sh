#!/bin/bash
set -e

if [[ ! -z "$@" ]]; then
    "$@"
elif [[ "$DATASETTE_IMPORT_DATA" -eq 1 ]]; then
    echo "Updating DB with data from API"
    python src/main.py
else
    exec datasette -p 8001 -h 0.0.0.0 db/servicemap.db
fi

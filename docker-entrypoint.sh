#!/bin/bash
set -e

if [[ ! -z "$@" ]]; then
    "$@"
elif [[ "$DATASETTE_IMPORT_DATA" -eq 1 ]]; then
    echo "Updating DB with data from API"
    python src/main.py
else
    exec datasette -p $PORT -h $HOST db/$DB
fi

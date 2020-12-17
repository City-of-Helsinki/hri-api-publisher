# HRI API Publisher

## Running locally without docker

### Prerequisites

* Python 3.9

### Install dependencies

    $ pip install -r requirements.txt

### Create database with data from api

    $ python src/main.py

### Run datasette

    $ datasette -p 8001 -h 0.0.0.0 db/servicemap.db


## Running with docker

### Create database

    $ sh import_data.sh

### Run docker

    $ docker-compose up --build

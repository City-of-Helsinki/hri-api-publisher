# HRI API Publisher

## Overview

This program is intended to offer an alternative way of using the data from the open APIs of the City of Helsinki. This is done by creating and offering user-friendly CSV -files available for download. These CSVs contain the same data as the API, but in a restructured format that allows usage with Excel for example.

## Running with docker

### Build image

    $ docker-compose build

### Create database

    $ sh import_data.sh

### Run docker

    $ docker-compose up --build

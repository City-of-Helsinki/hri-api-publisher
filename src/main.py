# For following, see:
# http://www.gevent.org/intro.html#monkey-patching
# https://github.com/gevent/gevent/issues/941
import gevent.monkey
gevent.monkey.patch_all()

import os
import json
import requests
import sqlite_utils
from flatten import flatten_jsons
from api_requests import collect_data_from_api

# Global constants
URL = os.environ['ROOT_URL']
db = sqlite_utils.Database(f"db/{os.environ['DB']}", recreate=True)

# Deprecated endpoints or these might not contain relevant data
restricted_keys = os.environ['RESTRICTED_ENDPOINTS']

def main():
    root_data = requests.get(URL).json()

    for api_key, api_url in root_data.items():
        print(f"Fetching data from: {api_url}")
        if api_key in restricted_keys:
            continue

        collected_results = collect_data_from_api(api_url)

        flattened_results = flatten_jsons(collected_results)

        db[api_key].insert_all(
            flattened_results,
            pk="id",
            replace=True
        )

if __name__ == '__main__':
    main()

import math
import grequests
import requests

ASYNC_CHUNK_SIZE = 50
PAGE_RESULT_COUNT = 20

def collect_data_async(collected_results, next_page_url, page_count):
    # Create list of pagination urls
    pagination_url_list = [next_page_url[:-1] + str(page_idx) for page_idx in range(2, page_count)]

    # Request pages in chunks
    for i in range(0, len(pagination_url_list), ASYNC_CHUNK_SIZE):
        print(".", end="")
        chunk = pagination_url_list[i:i+ASYNC_CHUNK_SIZE]

        rs = (grequests.get(c) for c in chunk)
        responses = grequests.map(rs)

        for response in responses:
            collected_results.extend(response.json()['results'])

    print("\n")
    return collected_results

def collect_data_from_api(api_url):
    # First page
    api_data = requests.get(api_url).json()
    next_page_url = api_data.get('next')
    collected_results = api_data['results']

    # Get the amount of pages
    page_count = math.ceil(api_data['count'] / PAGE_RESULT_COUNT)

    if next_page_url and page_count > 2:
        # Use asynchronous requesting for the rest of the pages if more than two pages
        collected_results = collect_data_async(collected_results, next_page_url, page_count)

    elif next_page_url:
        # Only two pages, just get the second one
        api_data = requests.get(next_page_url).json()
        next_page_url = api_data.get('next')
        collected_results.extend(api_data['results'])

    return collected_results

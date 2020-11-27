import pytest
from flatten import flatten_jsons

@pytest.fixture
def dummy_data():
    data = [
        {
            "id": "063c6150-ccc7-4886-b44b-ecee7670d064",
            "parent": None,
            "business_id": "2070757-2",
            "name": {
                "fi": "Suomen Kosmetologien Yhdistyksen Opiston Säätiö sr"
            },
            "municipality": None,
            "list_of_items": [
                2356,
                452765,
            ],
        },
        {
            "id": "43dc80f0-1c92-439d-8e31-42887904bcdb",
            "parent": None,
            "business_id": "0201242-7",
            "name": {
                "fi": "Helsingin Seurakuntayhtymä",
                "sv": "Helsingfors Kyrkliga Samfällighet"
            },
            "municipality": None,
            "list_of_items": [
                2356,
                452765,
                5246,
                456,
            ],
        },
    ]

    return data

def test_json_flattening_in_list(dummy_data):
    assert flatten_jsons(dummy_data) == [
        {
            "id": "063c6150-ccc7-4886-b44b-ecee7670d064",
            "parent": None,
            "business_id": "2070757-2",
            "name_fi": "Suomen Kosmetologien Yhdistyksen Opiston Säätiö sr",
            "name_sv": None,
            "municipality": None,
            "list_of_items_0": 2356,
            "list_of_items_1": 452765,
            "list_of_items_2": None,
            "list_of_items_3": None,
        },
        {
            "id": "43dc80f0-1c92-439d-8e31-42887904bcdb",
            "parent": None,
            "business_id": "0201242-7",
            "name_fi": "Helsingin Seurakuntayhtymä",
            "name_sv": "Helsingfors Kyrkliga Samfällighet",
            "municipality": None,
            "list_of_items_0": 2356,
            "list_of_items_1": 452765,
            "list_of_items_2": 5246,
            "list_of_items_3": 456,
        },
    ]

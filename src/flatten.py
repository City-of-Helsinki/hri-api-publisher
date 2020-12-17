import os
import json

DUMP_AS_JSON = os.environ['DUMP_AS_JSON'].split(',')

def flatten(x, result_item, name=''):
    """
        Removes nested structures from json.

        Flattens a list with name "name" to the root with names "name_0", "name_1", ..., "name_i",
        where i is the index of corresponding value in the list.

        Flattens a dict with name "name": {"fi": ..., "sv": ...} to the root with names "name_fi": ..., "name_sv": ...

        Alternatively dumps list/object with a specified name as json to a single root field.
    """
    if isinstance(x, dict):
        for field_name in DUMP_AS_JSON:
            if name.startswith(field_name):
                a = json.dumps(x)
                result_item = flatten(a, result_item, name)
                break
        else: # if no break
            for a in x:
                result_item = flatten(x[a], result_item, name + a + '_')
    elif isinstance(x, list):
        for field_name in DUMP_AS_JSON:
            if name.startswith(field_name):
                a = json.dumps(x)
                result_item = flatten(a, result_item, name)
                break
        else: # if no break
            i = 0
            for a in x:
                result_item = flatten(a, result_item, name + str(i) + '_')
                i += 1
    else:
        if isinstance(x, str):
            # Remove newlines to avoid malformed csv lines
            x = x.replace('\n', '')
        result_item[name[:-1]] = x
    return result_item

def normalize_json_fields(result_list):
    """
        Makes sure that each json contains the same fields.
        Adds them with None as value if any field is missing.
    """

    found_keys = set()
    for item in result_list:
        found_keys.update(item.keys())

    for item in result_list:
        for key in found_keys:
            if key not in item:
                item[key] = None

    return result_list

def flatten_jsons(data):
    """List format stays the same, flattens each json inside the list individually."""

    result_list = []
    for item in data:
        result_item = {}
        result_item = flatten(item, result_item)
        result_list.append(result_item)

    result_list = normalize_json_fields(result_list)

    return result_list

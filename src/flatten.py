
def flatten(x, result_item, name=''):
    """
        Removes nested structures from jsons.

        Flattens a list with name "name" to the root with names "name_0", "name_1", ..., "name_i",
        where i is the index of corresponding value in the list.

        Flattens a dict with name "name": {"fi": ..., "sv": ...} to the root with names "name_fi": ..., "name_sv": ...
    """
    if isinstance(x, dict):
        for a in x:
            result_item = flatten(x[a], result_item, name + a + '_')
    elif isinstance(x, list):
        i = 0
        for a in x:
            result_item = flatten(a, result_item, name + str(i) + '_')
            i += 1
    else:
        result_item[name[:-1]] = x
    return result_item

def normalize_json_fields(result_list):
    """Makes sure that each json contains the same fields. Adds them with None as value if any missing."""

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

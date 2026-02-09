#!/usr/bin/python3
"""Module for converting a Python object to a JSON string."""


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object."""
    import json
    return json.dumps(my_obj)

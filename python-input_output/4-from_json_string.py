#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string."""
    import json
    return json.loads(my_str)

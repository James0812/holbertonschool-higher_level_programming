#!/usr/bin/python3
"""Module for loading a Python object from a JSON file."""


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

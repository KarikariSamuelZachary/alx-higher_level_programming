#!/usr/bin/python3
"""
load_from_json_file module.

Contains a function that creates an Object from a json file
"""
import json


def load_from_json_file(filename):
    """Writes a JSON  Object to a text file."""
    with open(filename, 'r') as f:
        return json.load(f)

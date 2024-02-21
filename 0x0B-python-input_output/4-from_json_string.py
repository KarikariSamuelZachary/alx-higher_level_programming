#!/usr/bin/python3
"""from_json_string module

Contains a function that deserializes a json object
"""
import json


def from_json_string(my_str):
    """Returns JSON representation of an object"""
    return json.loads(my_str)

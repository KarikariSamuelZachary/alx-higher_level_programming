#!/usr/bin/python3
"""to_json_string module

Contains a function that serialzes an object
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    return json.dumps(my_obj)


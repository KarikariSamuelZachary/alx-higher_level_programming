#!/usr/bin/python3
"""is_same_class module

Contains a function that compares an object with an instance
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance
    of the class otherwise False
    """
    return type(obj) is a_class

#!usr/bin/python3
"""Lookup Module

Contains a lookup functon that displays all
the attributes and methods of an object in
a list form
"""


def lookup(obj):
    """Returns a list of attributes and methods in an object"""
    return dir(obj)

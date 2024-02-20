#!/usr/bin/python3
"""write_file module

This module contans a functon that writes a string to a test
file and returns number of written characters
"""


def write_file(filename="", text=""):
    """returns the number of characters in a text file"""
    with open(filename, "w") as f:
        return f.write(text)

#!/usr/bin/python3

"""append_write module

This module appends a string to the eof
of a file and returns the num of characters
"""


def append_write(filename="", text=""):
    """Returns the number of characters in a file"""
    with open(filename, "a") as f:
        return f.write(text)

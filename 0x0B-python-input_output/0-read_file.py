#!/usr/bin/python3
"""read_file module

This module contains a function that
reads a text file and prints it out to
stdout
"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

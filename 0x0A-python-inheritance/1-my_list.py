#!/usr/bin/python3
"""My list module

Contans a subclass My List that inherits
from the Base Class List
"""


class MyList(list):
    """Defines the MyList Class"""

    def print_sorted(self):
        """Prints the list but in sorted ascending order"""
        print(sorted(self))

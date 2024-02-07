#!/usr/bin/python3

"""
Square module

This module contains finction def for sq


"""


class Square():
    """Sqare Definition"""

    def __init__(self, size=0):
        """
        Constructor Definition

        Args:
            size(int): size of one side of the square

        Raises:
            TypeError: If the size is not gven as an integer
            ValueError: If the value of size is < than 0
        """

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

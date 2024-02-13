#!/usr/bin/python3

"""
This module contains a class that represent rectangles
"""


class Rectangle():
    """Rectangle Definiton"""
    def __init__(self, height=0, width=0):
        """Sets the attributes for the rectangle class

        Args:
            width (int) = width of the rectangle
            height (int) = height of the triangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width attrbute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >=0")
        else:
            raise TypeError("height must be an integer")

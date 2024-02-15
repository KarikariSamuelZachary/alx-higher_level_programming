#!/usr/bin/python3

"""
This module contains a class that represent rectangles
"""


class Rectangle():
    """Rectangle Definiton"""
    def __init__(self, width=0, height=0):
        """Sets the attributes for the rectangle class

        Args:
            width (int) = width of the rectangle
            height (int) = height of the triangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """the __str__ method of the Rectangle instance"""
        rectangle = ""
        if self.__width > 0 or self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.width + '\n'
        return rectangle[:-1]

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

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of a rectangle"""
        if self.__width and self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

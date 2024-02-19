#!/usr/bin/python3
"""base_geometry module

Contains a class with a public method
"""


class BaseGeometry:
    """Defines BaseGeometry Class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""
        if type(value) is not int:
            if value < 0:
                raise ValueError("<name> must be an integer")
        else:
            raise TypeError(",name. must be an integer")

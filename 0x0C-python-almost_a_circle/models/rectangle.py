#!/usr/bin/python3
"""Rectangle module.

Contains the Rectangle class that inherits from the base class "Base".
"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from Base and defines a Rectangle.

    Attributes:
        __width (int): the width of the rectangle, private.
        __height (int): the height of the rectangle, private.
        __x (int): the horizontal (x) padding of the rectangle, private.
        __y (int): the vertical (y) padding of the rectangle, private.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the default attributes of the Base object.

        Args:
            width (int): the needed width of the rectangle.
            height (int): the needed height of the rectangle.
            x (int): the needed horizontal (x) padding of the rectangle.
            y (int): the needed vertical (y) padding of the rectangle.
            id (int): the needed identifier of the Base object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """This method overrides the default behaviour of the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # width attribute getter and setter.
    @property
    def width(self):
        """Get and Set the width attribute of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height attribute getter and setter.
    @property
    def height(self):
        """Get and Set the height attribute of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get and Set the x attribute of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get and Set the y attribute of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints to stdout the Rectangle instance with the character #."""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates the Rectangle attributes.

        Args:
            args (list): attributes to be modified.
            kwargs (dict): other attributes to be modified.
        """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == 'id' and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }

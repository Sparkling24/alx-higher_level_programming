#!/usr/bin/python3
"""Rectangle class
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        c = ''
        if self.__height == 0 or self.__width == 0:
            return c
        for y in range(self.height):
            for x in range(self.width):
                c += '#'
            if y != self.height - 1:
                c += '\n'
        return c

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

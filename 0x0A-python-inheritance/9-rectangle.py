#!/usr/bin/python3
"""Create empty BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """Initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """Validates the value for int type."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

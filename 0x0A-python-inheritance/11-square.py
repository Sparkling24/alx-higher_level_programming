#!/usr/bin/python3
""" a class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square"""

    def __init__(self, size):
        """Initialize the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

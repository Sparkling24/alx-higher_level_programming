#!/usr/bin/python3
"""Create empty BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py)"""

    def __init__(self, width, height):
        """Initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

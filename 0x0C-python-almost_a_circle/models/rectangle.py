#!/usr/bin/python3
"""
class Rectangle: is the base for all other classes in this project
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def display(self):
        """Print a rectangle using #'s to stdout"""
        if self.__y:
            print("\n" * self.__y, end='')

        for i in range(self.__height):
            if self.__x:
                print(" " * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] (" + str(self.id) + ") " + str(
            self.__x) + "/" + str(self.__y) + " - " + str(
                self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        def update(self, *args): that assigns an argument to
        each attribute
        """
        if args:
            self.id = args[0] if 0 < len(args) else self.id
            self.width = args[1] if 1 < len(args) else self.width
            self.height = args[2] if 2 < len(args) else self.height
            self.x = args[3] if 3 < len(args) else self.x
            self.y = args[4] if 4 < len(args) else self.y
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

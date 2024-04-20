#!/usr/bin/python3
"""
class Square: iinherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square: inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size property
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args:
            self.id = args[0] if 0 < len(args) else self.id
            self.size = args[1] if 1 < len(args) else self.size
            self.x = args[2] if 2 < len(args) else self.x
            self.y = args[3] if 3 < len(args) else self.x
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        return self

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @classmethod
    def create(cls, **kwargs):
        """
        create method
        """
        if "x" not in kwargs or "y" not in kwargs:
            kwargs["x"] = 0
            kwargs["y"] = 0
        return cls(**kwargs)

#!/usr/bin/python3
"""MyList class inheriting from list class"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """prints the sorted list."""

        list_cpy = self.copy()
        list_cpy.sort()
        print("{}".format(list_cpy))

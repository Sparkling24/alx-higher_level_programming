#!/usr/bin/python3
"""
class Base: is the base for all other classes in this project.
"""
import json
import os


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id
        and set as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of instances as json strings into file"""
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(cls.to_dictionary(obj))
        with open("{:s}.json".format(cls.__name__), mode='w') as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj from a json string representation"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(3)
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        llist = []

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            instances = cls.from_json_string(f.read())

        for i, d in enumerate(instances):
            llist.append(cls.create(**instances[i]))

        return llist

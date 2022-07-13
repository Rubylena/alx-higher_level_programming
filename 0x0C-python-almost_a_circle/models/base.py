#!/usr/bin/python3
""" Define a base class """
import json


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".json"
        export_list = []
        with open(filename, "w") as new_file:
            if list_objs is None:
                return new_file.write("[]")
            else:
                for i in list_objs:
                    export_list.append(cls.to_dictionary(i))
                    # lo = [i.to_dictionary() for i in list_objs]
                new_file.write(cls.to_json_string(export_list))

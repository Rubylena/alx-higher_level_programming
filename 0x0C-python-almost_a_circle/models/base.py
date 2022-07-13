#!/usr/bin/python3
""" Define a base class """
import json
import csv
import turtle


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
                    # export_list.append(Base.to_dictionary(i))
                    export_list = [i.to_dictionary() for i in list_objs]
                new_file.write(Base.to_json_string(export_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """

        if (dictionary):
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keynames = ["id", "width", "height", "x", "y"]
                else:
                    keynames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=keynames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as csvfile:
                if cls.__name__ == "Rectangle":
                    keynames = ["id", "width", "height", "x", "y"]
                else:
                    keynames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=keynames)
                list_dicts = [dict([k, int(v)] for k, v in
                              d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        color_size = len(color_list)
        color_index = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(90)
        turtle.forward(screen_height/2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()

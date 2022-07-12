#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return ('[{}] ({:d}) {:d}/{:d} - {:d}'.format(Square.__name__,
                                                      self.id, self.x,
                                                      self.y, self.width))

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                # enumerate gives both the index and value respectively
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        return ({'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y})

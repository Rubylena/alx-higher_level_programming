#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif (value <= 0):
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif (value < 0):
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif (value < 0):
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.height * self.width

#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Represent a square '''

    def __init__(self, size):
        ''' Intializing an instance of a class to raise error '''

        self.__size = size

    @property
    def size(self):
        ''' getting the value of size '''

        return (self.__size)

    @size.setter
    def size(self, value):
        ''' setting the value of size and making sure there are no errors '''

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size == value

    def area(self):
        ''' method to check for area of a square '''

        area = self.__size ** 2
        return (area)

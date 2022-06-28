#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Intializing an instance of a class to raise error '''

    def __init__(self, size):
        self.__size = size
    ''' getting the value of size '''

    @property
    def size(self):
        return (self.__size)

    ''' setting the value of size and making sure there are no errors '''

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.size == value

    ''' method to check for area of a square '''

    def area(self):
        area = self.size ** 2
        return (area)

    ''' method to print hashes according to square size'''

    def my_print(self):
        if (self.size == 0):
            print()
        for x in range(self.size):
            print(self.size * '#')

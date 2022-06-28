#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Represent a square '''

    def __init__(self, size):
        ''' Intializing an instance of a class to raise error '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

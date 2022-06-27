#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Intializing and instance of a class to raise error '''

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif(size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Represent a square.'''

    def __init__(self, size):
        ''' intializing a class instance.

        Args:
            size (int): The size of the new square.
        '''

        self.__size = size

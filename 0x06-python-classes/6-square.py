#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Represent a square '''

    def __init__(self, size, position):
        ''' Intializing an instance of a class to raise error '''

        self.__size = size
        self.__position = position

    @property
    def size(self):
        ''' getting/setting the value of size '''

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        self.__size == value

    @property
    def position(self):
        ''' getting the value of size '''

        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position == value

    def area(self):
        ''' method to check for area of a square '''

        area = self.__size ** 2
        return (area)

    def my_print(self):
        ''' method to print hashes according to square size'''

        if (self.__size == 0):
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()

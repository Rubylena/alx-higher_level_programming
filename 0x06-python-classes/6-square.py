#!/usr/bin/python3
''' defining a class - Square '''


class Square:
    ''' Intializing an instance of a class to raise error '''

    def __init__(self, size, position):
        self.__size = size
        self.__position = position

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
        self.__size == value

    ''' getting the position of square'''

    @property
    def position(self):
        return (self.__position)

    ''' setting the value of size and making sure there are no errors '''

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position == value

    ''' method to check for area of a square '''

    def area(self):
        area = self.__size ** 2
        return (area)

    ''' method to print hashes according to square size'''

    def my_print(self):
        if (self.__size == 0):
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()

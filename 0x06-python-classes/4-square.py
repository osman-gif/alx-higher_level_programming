#!/usr/bin/python3
""" creates a class Square that defines a square """


class Square:

    """ This class is to model a square """

    def area(self):

        """ Returns the current squared area """
        return self._size ** 2

    @property
    def size(self):

        """ gets the size of the current area """
        return self._size

    @size.setter
    def size(self, _size):

        """ sets the current size """
        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._size = _size

    def __init__(self, _size=0):

        """ Initilaizes an instance of square class """

        self._size = _size

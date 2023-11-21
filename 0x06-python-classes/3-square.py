#!/usr/bin/python3
""" Creates class Square that defines a square  """


class Square:

    """ This class is to model a square """

    def area(self):

        """ Returns Current square area """

        return self._size ** 2

    def __init__(self, _size=0):

        """ Initializes an instance of the square class """

        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._size = _size

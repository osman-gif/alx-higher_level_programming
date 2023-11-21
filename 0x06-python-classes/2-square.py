#!/usr/bin/python3
""" Creates a class Square that defines a square """


class Square:
    """ This class is to model a square """

    def __init__(self, __size=0):

        """ Initializes an instance of the class Square """
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

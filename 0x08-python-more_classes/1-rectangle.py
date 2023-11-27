#!/usr/bin/python3

""" This module creates an ampty class that models a rectangle """


class Rectangle:
    """ This class Models a simple rectangle """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ a proprety to return the width attribute """
        return self._width

    @width.setter
    def width(self, value):
        """ a property to first check the width attribue if its not < 0 and
        that it is an integer """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ a proprety to return the height attribute """
        return self._height

    @height.setter
    def height(self, value):
        """ a property to first check the height attribue if its not < 0 and
        that it is an integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

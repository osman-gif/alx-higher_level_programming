#!/usr/bin/python3
""" This module defines a class called BaseGeometry """


class BaseGeometry:
    """ This is a class that does nothing """

    def area(self):
        """ This Function raises an exception with this
        message (area() is not implemented)"""
        raise Exception("area() is not implemented")

#!/usr/bin/python3
""" This module defines a method called is_same_class. """


def is_same_class(obj, a_class):
    """ This is a method that receives 2 arguments
    the first argument is and object and the second
    is a class, this function returns true of the
    object is an instance of the provided class
    otherwise returns false. """
    return isinstance(type(obj),(a_class))

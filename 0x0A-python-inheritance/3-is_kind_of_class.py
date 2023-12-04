#!/usr/bin/python3
""" This module defines a function that return true or false according
to some logic """


def is_kind_of_class(obj, a_class):
    """ This function that recieves an object and
    a class, if object is instance of that class or
    a class that inherits from that class then returns
    True otherwise returns false """
    return isinstance(obj, a_class)

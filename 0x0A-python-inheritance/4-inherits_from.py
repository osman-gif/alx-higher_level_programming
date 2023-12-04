#!/usr/bin/python3
""" This module defines a function that recieves
an object and a class, then check if  that object's type
is of a class that inherits from the class (the second argument)
"""


def inherits_from(obj, a_class):
    """ This function recieve an object and a class as
    arguments, and returns true if the object's type
    is of a class that inherits from the class (the second argument)
    otherwise returns False """
    return issubclass(type(obj), a_class) and not (type(obj) is a_class)

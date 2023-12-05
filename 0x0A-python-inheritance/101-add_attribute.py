#!/usr/bin/python3
""" This module defines a function that add an attribute to an
object """


def add_attribute(obj, name, value):
    """ This function recieves and object and it tries to add
    a new attriute to it. if it did not succeed a rasie
    a TypeError exceptiton with the message (can't add new attribute """

    if type(obj) in [object, list, set, tuple, str, int, float, bool, dict]:
        raise TypeError("can't add new attribute")
    obj.name = value

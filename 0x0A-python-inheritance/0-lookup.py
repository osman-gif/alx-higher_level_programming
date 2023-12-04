#!/usr/bin/python3

""" This module defines a function that receives an object and
return all the attributes and methods of that object """


def lookup(obj):

    """ This function receives an object and return all the
    attrubutes associated with that object"""
    return dir(obj)

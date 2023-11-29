#!/usr/bin/python3

""" This module contains a function that addes two integers """


def add_integer(a, b=98):
    """
    This function adds two integers
    """
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif isinstance(a, int):
        pass

    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    elif isinstance(b, int):
        pass

    return a + b

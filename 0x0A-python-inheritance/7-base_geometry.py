#!/usr/bin/python3
""" This module defines a class called BaseGeometry """


class BaseGeometry:
    """ This is a class that defines two functions,
    function area:
        raise an exception.
    and the integer_validator fucntion:
        validate a value.
    """

    def area(self):
        """ This Function raises an exception with this
        message (area() is not implemented)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This Function validates a value:
        If value is not an integer: raise a TypeError
        if value is less or equal to 0: raise a ValueError
        """

        if name and value:
            if not (type(value) is int):
                raise TypeError(f"{name} must be an integer")
            elif value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError("BaseGeometry.integer_validator() missing 2 required positional arguments: 'name' and 'value'")

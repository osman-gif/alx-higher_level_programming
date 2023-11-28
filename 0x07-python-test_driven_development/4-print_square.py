#!/usr/bin/python3
""" This module defines a function (print_function(int) that recieve
an int as an argument and print square with character # """


def print_square(size):
    """ This function prints a square with the character # of size
    (size) """

    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            if size < 0.0:
                raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise TypeError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")

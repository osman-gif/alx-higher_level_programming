#!/usr/bin/python3
""" This module defines a class called MyInt that inherits
from int class, and have its behavior of == and != inverted
"""


class MyInt(int):
    """ This class inherits from int class and invert its ==
    and != operators """

    def __init__(self, num):
        """ This function Initializes the MyInt instance """
        self.num = num

    def __eq__(self, other):
        """ This function returns False if
        its arguments equal and returns
        True other wise """

        return self.num != other

    def __ne__(self, other):
        """ This function returns True if its arguments are
        equal else it returns Flase """
        return self.num == other

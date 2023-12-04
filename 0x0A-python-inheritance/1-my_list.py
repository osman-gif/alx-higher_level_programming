#!/usr/bin/python3

""" This module defines a class that inherts from list
class and returns a list in ordered form. """


class MyList(list):
    """ This class inherits from list and returns the list ordered form. """

    def print_sorted(self):
        """ This function returns an ordered list without affecting the
        original list."""
        print((sorted(self)))

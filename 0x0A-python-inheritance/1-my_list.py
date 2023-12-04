#!/usr/bin/python3

""" This module defines a class that returns a list """


class MyList(list):
    """ This class inherits from list and returns the list ordered """

    def print_sorted(self):
        """ This function returns an ordered list """
        print((sorted(self)))

#!/usr/bin/python3

""" This module define a function that appends a text
at the end of a file """


def append_write(filename="", text=""):
    """ This function appends text to the end
    of a file (filename) """

    with open(filename, 'a', text) as f:
        appended = f.write(text)
        return appended

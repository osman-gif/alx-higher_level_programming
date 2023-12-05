#!/usr/bin/python

""" This module defines a function that opens a file
and write to it """


def write_file(filename="", text=""):
    """ This function opens a file and write it, if
    the file do not exist it creates it, and it return
    the number of characters writn """

    with open(filename, 'w+', encoding="utf-8") as f:
        writen_data = f.write(text)
        return writen_data

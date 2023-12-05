#!/usr/bin/python3

""" This module defines a fuction that read from
a file and return the content read """


def read_file(filename=""):
    """ This function reads a file and return
    the content it read """
    
    data = ""
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end='')

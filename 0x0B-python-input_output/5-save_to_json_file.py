#!/usr/bin/python3
""" This module defines a function that writes
an Object to a text file, using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ This function writes and object to a text file,
    using a JSON representaion """

    with open(filename, 'w') as file:
        return json.dump(my_obj, file)

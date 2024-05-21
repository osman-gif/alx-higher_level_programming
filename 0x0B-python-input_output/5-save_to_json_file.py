#!/usr/bin/python3
""" This module defines a function that writes
an Object to a text file, using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ This function takes a python object, convet it to json and then write it to a json file"""

    with open(filename, 'w') as file:
        return json.dump(my_obj, file)

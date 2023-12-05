#!/usr/bin/python3
""" This module defines a function that convert string
to json format """


import json


def from_json_string(my_str):
    """ This function recieves a python object
    (string) and returns the json represntation
    of that object """

    j = json.loads(my_str)
    return ((j))

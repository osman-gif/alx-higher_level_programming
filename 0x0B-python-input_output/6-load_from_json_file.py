#!/usr/bin/python3
""" This module defines a function that creates an Object
from a JSON file"""


import json


def load_from_json_file(filename):
    """ This a function that loads json file and return
    its python representation
    """

    with open(filename) as file:
        return json.load(file)

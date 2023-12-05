#!/usr/bin/python3

""" This module defines a function that convert
json to python string """


import json


def to_json_string(my_obj):
    """ This function recieves json object
    and returns a python string representaion of
    the json object """

    return json.dumps(my_obj)

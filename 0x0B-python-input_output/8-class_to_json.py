#!/usr/bin/python3
""" This module defines function that returns
the dictionary description with simple data structure
for JSON serialization of an object """


import json


def class_to_json(obj):
    """ function that returns
    the dictionary description with simple data structure
    for JSON serialization of an object"""

    return json.loads(obj.__dict__)

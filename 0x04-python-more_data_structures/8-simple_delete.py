#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    new = a_dictionary.copy()
    for i in new.keys():
        if key == i:
            del a_dictionary[key]
    return a_dictionary

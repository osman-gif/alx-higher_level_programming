#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    if a_dictionary is None:
        return None
    new = a_dictionary.copy()
    for i in new.keys():
        if key == i:
            a_dictionary[i] = value
        else:
            a_dictionary[key] = value
    return a_dictionary

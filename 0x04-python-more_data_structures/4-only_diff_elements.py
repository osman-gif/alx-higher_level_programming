#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set_1.difference(set_2)

    for i in set_2.difference(set_1):
        new.add(i)
    return new

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    if my_list is None:
        return None
    big = 0

    for i in my_list:
        if i is None:
            return None
        if i > big:
            big = i
    return (big)

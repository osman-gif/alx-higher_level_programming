#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0

    for i in my_list:
        if not int(i):
            continue
        if i > big:
            big = i
    return (big)

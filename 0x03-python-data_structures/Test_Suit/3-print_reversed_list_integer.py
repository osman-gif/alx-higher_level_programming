#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    reversed_list = reversed(my_list)
    for num in reversed_list:
        print("{:d}".format(num))

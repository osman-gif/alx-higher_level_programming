#!/usr/bin/python3

def safe_print_integer(value):
    res = False
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        res = False
    except TypeError:
        res = False
    else:
        res = True
    return res

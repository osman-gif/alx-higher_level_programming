#!/usr/bin/python3

def safe_print_integer_err(value):
    res = False
    try:
        print("{:d}".format(value))
    except ValueError as verr:
        res = False
        print(verr, file=sys.stderr)
    except TypeError as terr:
        res = False
        print(terr, file=sys.stderr)
    else:
        res = True
    return res

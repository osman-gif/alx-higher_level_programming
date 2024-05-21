#!/usr/bin/python3

def set_tuple(tuple_c= ()):
    if len(tuple_c) == 0:
        tuple_c = 0, 0
    elif len(tuple_c) == 1:
        tuple_c = tuple_c[0], 0
    elif len(tuple_c) > 2:
        tupe_a = tuple_c[0], tuple_c[1]
    return tuple_c

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = set_tuple(tuple_a)
    tuple_b = set_tuple(tuple_b)

    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


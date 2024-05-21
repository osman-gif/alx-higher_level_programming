#!/usr/bin/python3
def uniq_add(my_list=[]):

    new = []
    sum = 0

    for x in my_list:
        if x not in new:
            sum = sum + x
            new.append(x)

    return sum

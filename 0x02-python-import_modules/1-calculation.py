#!/usr/bin/python3

import calculate_1 as cal

a = 10
b = 5

if __name__ == "__main__":

    summ = cal.add(a, b)
    print("{} + {} = {}".format(a, b, summ))
    sub = cal.sub(a, b)
    print("{} - {} = {}".format(a, b, sub))
    mul = cal.mul(a, b)
    print("{} * {} = {}".format(a, b, mul))
    div = cal.div(a, b)
    print("{} / {} = {}".format(a, b, int(div)))

#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        cr = ord(ch)
        if cr > 96 and cr < 123:
            cr = cr - 32
        print("{}".format(chr(cr)), end="")
    print()

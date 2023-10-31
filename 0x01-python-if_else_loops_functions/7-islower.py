#!/usr/bin/python3
def islower(c):
    ch = ord(c)

    if ch > 64 < 91:
        return False
    elif ch > 96 and ch < 123:
        return True

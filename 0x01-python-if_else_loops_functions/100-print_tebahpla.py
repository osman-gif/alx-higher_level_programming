#!/usr/bin/python3
for ch in range(-92, -63):
    if ch < -64 and ch > -91:
        if (ch * -1) % 2 == 0:
            cs = 32
        else:
            cs = 0
        print("{}".format(chr((ch * -1) + cs)), end="")

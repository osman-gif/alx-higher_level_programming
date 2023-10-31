#!/usr/bin/python3
for n in range(100):
    if n < 10:
        n = "0" + str(n)
    print("{}".format(n), end="")
    if int(n) == 99:
        n = "\n"
    else:
        n = ", "
    print("{}".format(n), end="")

#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    num = 0

    for i in range(0, x):
        try:
            print("{:d}".format(int(my_list[i])), end="")
            count += 1
        except ValueError:
            continue
        except TypeError:
            continue
        except IndexError:
            raise
    print("")

    return (count)

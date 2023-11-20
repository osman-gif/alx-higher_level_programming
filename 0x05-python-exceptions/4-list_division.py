#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    new_list = []

    for i in range(0, list_length):
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            div = float(a / b)
        except TypeError:
            div = 0
            print("wrong type")
        except ValueError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        finally:
            new_list.append(div)
    return new_list

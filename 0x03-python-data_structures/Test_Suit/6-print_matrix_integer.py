#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[i])):
            delim = " "
            if j >= len(matrix[i])-1:
                delim = ""
            print("{}".format(matrix[:][i][j]), end=delim)
        print()

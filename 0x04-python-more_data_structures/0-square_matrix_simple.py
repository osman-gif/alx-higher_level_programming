#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[num**2 for num in matrix[idx]] for idx in range(len(matrix))]
    return (new)

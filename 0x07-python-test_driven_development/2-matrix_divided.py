""" This module defines a function that devides all elements of
the matrix by div """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix """

    lst = []
    raw_len = len(matrix[0])
    new_mat = [row[:] for row in matrix]
    message = "matrix must be a matrix (list of lists) of integers/floats"

    for x in range(len(matrix)):
        if not isinstance(matrix[x], list):
            raise TypeError(message)
        for i in range(len(matrix[x])):
            new_mat[x][i] = matrix[x][i]

    if not isinstance(div, int):
        if not isinstance(div, float):
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for x in range(len(matrix)):
        if type(matrix) is not list:
            raise TypeError(message)

        if len(matrix[x]) != raw_len:
            raise TypeError(
                    "Each row of the matrix must have the same size")

        for i in range(len(matrix[x])):
            if not isinstance(matrix[x], list):
                raise TypeError(message)

            if not isinstance(matrix[x][i], int):
                if not isinstance(matrix[x][i], float):
                    raise TypeError(message)

            new_mat[x][i] = round(matrix[x][i] / div, 2)
    return new_mat

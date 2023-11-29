""" This module defines a function that devides all elements of
the matrix by div """


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix """

    lst = []
    raw_len = len(matrix[0])
    new_mat = [row[:] for row in matrix]
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    for x in range(len(matrix)):
        if not isinstance(matrix[x], list):
            raise TypeError(message)

        if len(matrix[x]) != raw_len:
            raise ValueError(
                    "Each row of the matrix must have the same size")

        for i in range(len(matrix[x])):
            if isinstance(div, int) or isinstance(div, float):
                pass
            else:
                raise TypeError("div must be a number")

            if div == 0:
                raise ZeroDivisionError("division by zero")
            if isinstance(matrix[x][i], int):
                new_mat[x][i] = round(matrix[x][i] / div, 2)
            elif isinstance(matrix[x][i], float):
                new_mat[x][i] = round(matrix[x][i] / div, 2)
            else:
                raise TypeError(message)

    return new_mat

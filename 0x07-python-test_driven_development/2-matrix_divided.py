#!/usr/bin/python3
"""
    2-matrix_divided.py
    Function that divides all elements of a matrix
    return [ [matrix[0][0]/div ... ] [matrix[1][0]/div ...] ...]
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
        return [ [matrix[0][0]/div ... ] [matrix[1][0]/div ...] ...]
    """
    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    m2 = "Each row of the matrix must have the same size"
    m3 = "div must be a number"
    m4 = "division by zero"
    if type(matrix) != list or any(type(a) != list for a in matrix) \
       or len(matrix) == 0 or any(len(a) == 0 for a in matrix):
        raise TypeError(m1)

    for c in matrix:
        for b in c:
            if type(b) != int and type(b) != float:
                raise TypeError(m1)

    if any((len(matrix[0]) != len(d)) for d in matrix):
        raise TypeError(m2)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(m3)

    if div == 0:
        raise ZeroDivisionError(m4)

    return [[round(i / div, 2) for i in j] for j in matrix]

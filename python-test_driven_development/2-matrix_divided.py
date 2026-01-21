#!/usr/bin/python3
"""Module that provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): list of lists of integers/floats
        div (int/float): number to divide by

    Returns:
        list of lists: new matrix with divided elements rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
                   or rows have different sizes,
                   or div is not a number
        ZeroDivisionError: if div is 0
    """
    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix type
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(elem, (int, float)) for elem in row)
                    for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows have same size
    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Divide elements and round to 2 decimals
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix


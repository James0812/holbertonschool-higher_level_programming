#!/usr/bin/python3
"""Square class defined that calculates the area of a square"""


class Square:
    """__init__method that initialize a square class

    Args:
        size: size of square
    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of square

        Return:
            returns the area of the square
        """

        return self.__size * self.__size

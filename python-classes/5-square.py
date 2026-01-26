#!/usr/bin/python3
"""Defines a square class with size property, area, and printing capabilities."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        self.size = size  # utilise le setter pour validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)

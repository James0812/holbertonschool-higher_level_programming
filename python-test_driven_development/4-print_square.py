#!/usr/bin/python3
"""Module 4-print_square: prints a square with the character #"""

def print_square(size):
    """
    Prints a square of the given size using the '#' character.

    Args:
        size (int): the length of the square's sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    # Vérification du type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Vérification de la valeur
    if size < 0:
        raise ValueError("size must be >= 0")

    # Impression de la ligne de la taille demandée
    for _ in range(size):
        print("#" * size)

#!/usr/bin/python3
"""Module that prints text with 2 new lines after '.', '?', and ':'"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            line = text[start:i + 1].strip()
            print(line)
            print()  # la deuxième ligne vide
            start = i + 1

    remaining = text[start:].strip()
    if remaining:
        # Ici on utilise 'end=""' pour ne pas ajouter un '\n' final supplémentaire
        print(remaining, end="")

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

    # Liste des caractères après lesquels on met 2 nouvelles lignes
    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # Découpe la partie jusqu'au séparateur inclus
            line = text[start:i + 1].strip()
            print(line)
            print()  # seconde ligne vide
            start = i + 1  # début de la prochaine portion

    # Imprimer le reste du texte s'il y en a
    remaining = text[start:].strip()
    if remaining:
        print(remaining)

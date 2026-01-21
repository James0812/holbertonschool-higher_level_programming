#!/usr/bin/python3
"""Module that provides a function to print text with 2 new lines after
   each '.', '?' or ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): the input text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    start = 0

    for index, char in enumerate(text):
        if char in delimiters:
            # slice the part to print, strip spaces at start/end
            segment = text[start:index + 1].strip()
            if segment:
                print(segment)
                print()
            start = index + 1

    # print any remaining text after the last delimiter
    last_segment = text[start:].strip()
    if last_segment:
        print(last_segment)

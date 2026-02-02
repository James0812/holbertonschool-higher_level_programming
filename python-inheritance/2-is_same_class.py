#!/usr/bin/python3
"""
Module 2-is_same_class
Defines a function that checks if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified
    class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

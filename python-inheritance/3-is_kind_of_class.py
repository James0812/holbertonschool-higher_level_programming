#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance of, or
inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance or subclass instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list and adds a print_sorted method.
"""


class MyList(list):
    """
    Represents a list that can print its elements in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))

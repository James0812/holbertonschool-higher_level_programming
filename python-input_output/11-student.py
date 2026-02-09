#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only include those attributes.
        Otherwise, return all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        filtered = {}
        for key in attrs:
            if key in self.__dict__:
                filtered[key] = self.__dict__[key]
        return filtered

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from json.

        json is a dictionary where keys are attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)

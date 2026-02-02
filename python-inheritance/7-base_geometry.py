#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with methods area() and integer_validator().
"""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with methods area() and integer_validator().
"""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

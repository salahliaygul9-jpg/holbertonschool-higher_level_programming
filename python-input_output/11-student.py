#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """Class that defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only include those attributes.
        Otherwise, include all public attributes.
        """
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        json is a dictionary where keys are attribute names
        and values are the values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)

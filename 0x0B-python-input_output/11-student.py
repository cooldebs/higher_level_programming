#!/usr/bin/python3
""" Module "11-student"
"""


class Student:
    """ Defines a Student class """
    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for t in attrs:
            try:
                new_dict[t] = self__dict__[t]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception:
                pass

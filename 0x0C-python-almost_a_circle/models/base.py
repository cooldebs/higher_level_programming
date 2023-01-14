#!/usr/bin/python3
""" The Base module
"""


import json
import csv


class Base:
    """ Definition of the Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

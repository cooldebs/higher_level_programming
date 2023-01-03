#!/usr/bin/python3
"""
The "0-add_integer" module.

The module defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

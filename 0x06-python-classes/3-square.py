#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the Square object

        Args: size(int) - represents the size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of a square

        Returns: Area of a square
        """
        return self.__size ** 2

#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the Square Object

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

    @property
    def size(self):
        """Gets the size attribute
        Returns: __size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size attribute

        Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Calculates the area of a square
        Return: Area of the square
        """

        return self.__size ** 2

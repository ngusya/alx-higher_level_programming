#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """"Defines a new square"""

    
    def __init__(self, size=0):
        """Initializes the square
        Args:
         size(int): Size of the square
         """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

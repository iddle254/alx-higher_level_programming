#!/usr/bin/python3
"""
Contains the class Square and subclass
"""

Rectangle = __import__('9-rectangle').Rectangle

"""Square class that inherits from Rectangle that inherits Rectangle"""
class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

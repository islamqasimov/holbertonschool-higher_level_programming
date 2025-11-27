#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Subclass of BaseGeometry that represents Rectangle.
    """
    def __init__(self, width, heigth):
        self.integer_validator("width", width)
        self.__heigth = self.integer_validator("heigth", heigth)
        self.__width = width
        self.__heigth = heigth

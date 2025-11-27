#!/usr/bin/python3
"""
Rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass of BaseGeometry that represents Rectangle.
    """
    def __init__(self, width, heigth):
        self.integer_validator("width", width)
        self.__heigth = self.integer_validator("heigth", heigth)
        self.__width = width
        self.__heigth = heigth

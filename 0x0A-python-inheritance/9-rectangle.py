#!/usr/bin/python3
""" This module defines a class that inherit from antoher
class called BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """ This class inherits from the BaseGeomtry class
    and validate the width and height attribues through
    the inherited method validator"""
    def __init__(self, width, height):
        """ This function initilizes the Rectangle class
        """

        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ This function returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

#!/usr/bin/python3
""" This module define a class that inherits form
Rectangle class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This class models a square object with attribues
    area """
    def __init__(self, size):
        """ This function initializes the Square class"""
        self.__size = size

        super().integer_validator("size", self.__size)

    def area(self):
        """ This function returns the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ This function print square detals """
        return f"[Square] {self.__size}/{self.__size}"

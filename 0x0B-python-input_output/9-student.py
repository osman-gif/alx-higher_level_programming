#!/usr/bin/python3
""" This module defines a class that models a student
object with one function"""


class Student:
    """ This class models a student, with three attrubues:
    first_name, last_name and age, and it has method
    called to_json that returns json-like object """

    def __init__(self, first_name, last_name, age):
        """ This function initializes all class instances
        attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    to_json(self):
        return self.__dict__

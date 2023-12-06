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

    def to_json(self, attrs=""):
        """ This function returns json-like dict representation
        of the class object """
        new_dict = {}
        old_dict = self.__dict__
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is str:
                    if attr in list(old_dict.keys()):
                        new_dict[attr] = old_dict[attr]
                else:
                    return old_dict
        else:
            return old_dict

        return new_dict

    def reload_from_json(self, json):
        """ This function recieves a json object
        and replaces all the attributes of the instance
        of the class """

        old_dict = self.__dict__
        o_keys = old_dict.keys()
        j_keys = json.keys()

        for j_key in j_keys:
            if j_key in o_keys:
                old_dict[j_key] = json[j_key]

#!/usr/bin/python3

"""
This Module defines a class base which is the base class for all
the other class to inherit from
"""
from models.base import Base
import json


class Base:
    """
    This class represent the super class (base class) to all the other
    classes that will be created later, it has 1 private attribue, the
    goal of this class is to mangage id attribute in all its subclass
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This method initializes the Base class, with one
        opitional argument and zero positional argument"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This class method returns the JSON string representation
        of list_dictionaries:
            list_dictionaries is a list of python dictionaries,
            if list_dictionaries is None or empty, return the string: "[]"
            Otherwise, return the JSON string representation of
            list_dictionarie
        """

        if list_dictionaries and list_dictionaries != []:
            json_dict = json.dumps(list_dictionaries)
            return json_dict
        else:
            return "[]"

    @classmethod
    def load_from_file(cls):
        """
        This class method returns a list of instances:
        The instances type depends on the cls
        (current class using this method), If the file doesn’t exist,
        return an empty list.
        Otherwise, return a list of instances
        """

        json_str_list = None
        # objs_string = None
        instances_list = None

        with open(f"{cls.__name__}.json") as file:
            json_str_list = file.read()
            json_str_list = cls.to_json_string(json_str_list)
        print(json_str_list)
        instances_list = cls.from_json_string(json_str_list)
        print(instances_list[0])
        # instances_list.append(cls.create(objs_str))

        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method writes the JSON string representation
        of list_objs to a file:
            #(list_objs) is a list of instances who inherits of
            Base - example: list of Rectangle or list of Square instances
            #If list_objs is None, save an empty list
            #The filename must be: <Class name>.json - example: Rectangle.json
            #You must use the static method to_json_string (created before)
            #You must overwrite the file if it already exists
        """

        objs_list = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):

                objs_list.append(list_objs[i].__dict__)
        with open(f"{cls.__name__}" + ".json", 'w') as file:
            file.write(str(objs_list))

    @staticmethod
    def from_json_string(json_string):
        """
        This static method returns the list of the
        JSON string representation (json_string):
            #json_string is a string representing a list of dictionaries
            #If json_string is None or empty, return an empty list
            #Otherwise, return the list represented by json_string
        """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This class method returns an instance with
        all attributes already set:
            **dictionary can be thought of as a double
            pointer to a dictionary.
            To use the update method to assign all attributes,
            #you must create a “dummy” instance before:
                -Create a Rectangle or Square instance with “dummy”
                 mandatory attributes (width, height, size, etc.)
                -Call update instance method to this “dummy”
                instance to apply your real values
            #You must use the method def update(self, *args, **kwargs)
            #**dictionary must be used as **kwargs of the method update
        """

        rectangle = cls(1, 2)
        rectangle.update(*[], **dictionary)
        return rectangle

#!/usr/bin/python3

"""
This module defines a class (Square) that inherits
from the class (Rectangle)
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class Inherit from the Rectangle method, it will
    overload __str__ method
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This initializes the class with four
        arguments, three are optional arguments and one
        positional
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        This method updates the square instances
        with the (args) values or (kwargs) values:
        - args is a list of non-keywarded argument:
            first argument should be id
            second argument should be size
            third argument should be x
            forth argument should be y
        - kwargs can be thought of as a double pointer
          to a dictionary, and it must be skipped if args
          exits and is not empty
        """

        if args and args is not None:
            keys = list(self.__dict__.keys())
            id_key = keys[-1]
            size_key = keys[0]
            keys = keys[3:-1]
            keys.insert(0, id_key)
            keys.insert(1, size_key)

            for idx, item in enumerate(args):
                self.__dict__[keys[idx]] = item
        else:
            for k, v in kwargs.items():
                keys = list(self.__dict__.keys())
                match(k):
                    case 'size':
                        self.__dict__[keys[0]] = v
                    case 'width':
                        self.__dict__[keys[1]] = v
                    case 'height':
                        self.__dict__[keys[2]] = v
                    case 'x':
                        self.__dict__[keys[3]] = v
                    case 'y':
                        self.__dict__[keys[4]] = v
                    case 'id':
                        self.__dict__[keys[5]] = v

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Square.
        """

        current_dict = self.__dict__
        from_keys = list(self.__dict__.keys())
        to_keys = ['id', 'size', 'x', 'y']
        new_dict = {}

        for idx, item in enumerate(to_keys):
            for k, v in self.__dict__.items():
                if item in k:
                    new_dict[item] = v
        return new_dict

    @property
    def size(self):
        """ This size property getter return the size of the Square.
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
        This size property setter initializes the width
        and height with the same value of size
        """

        if (type(size)) is int:
            if size > 0:
                self.__size = size
            else:
                raise ValueError("size must be > 0")
        else:
            raise TypeError("size must be an integer")

    def __str__(self):
        """
        This method returns a string that represent square
        object.
        """
        return f"[Square] ({self.id}) {super().x}/{super().y} - {self.size}"

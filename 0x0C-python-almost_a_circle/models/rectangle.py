#!/usr/bin/python3

"""
This module defines a class that models a rectangle, This class
aslo inherits from the (Base) class with its method and
attributes
"""

from models.base import Base

import json


class Rectangle(Base):
    """
    This class inherits from (Base) class and
    it models a rectangle, with width and height as
    positional arguments and x, y and id as
    optional arguments
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method initializes the Rectangle class
        with 2 positional arguments and 3 optionl
        arguments, the (id) argument will be initialized
        via the super class (Base class)
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        This getter method returns the width of Rectangle object
        It acts as a getter to the width private attribute(__width)
        of the Rectangle instance (object)
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        This setter method validate the width attributes
        befor assigning it to the private instance
        attribute(width) of the Rectangle instance (object)
        """

        if (type(width)) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        This getter method returns the height of Rectangle object
        It acts as a getter to the height private attribute(__height)
        of the Rectangle instance (object)
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        This setter method validate the height attributes
        befor assigning it to the private instance
        attribute(__height) of the Rectangle instance (object)
        """

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        This setter method returns the private instance (__x)
        of Rectangle objectIt acts as a getter to the x private
        attribute(__x) of the Rectangle instance (object)
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        This getter method validate the private instance (__x) attribute
        befor assigning it to the private instance
        attribute(__x) of the Rectangle instance (object)
        """

        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError(f"x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        This getter method returns the private instance (__y)
        of Rectangle objectIt acts as a getter to the x private
        attribute(__y) of the Rectangle instance (object)
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        This setter method validate the private instance (__y) attribute
        befor assigning it to the private instance
        attribute(__y) of the Rectangle instance (object)
        """

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError(f"y must be an integer")

    def area(self):
        """
        This method calculates and returns the area of
        the rectangle based on width and height
        """

        return self.width * self.height

    def display(self):
        """
        This method desplays the rectangle,
        according to the x and y coordinates
        """

        for y in range(self.y):
            print('')
        for w in range(0, self.height):
            for x in range(self.x):
                print(' ', end='')
            for h in range(0, self.width):
                print("#", end='')
            print('')

    def __str__(self):
        """
        This method prints the Rectangle instance in a
        neat way, it returns a string that represent the
        rectangle and its attribues
        """
        return f"""[Rectangle] ({self.id}) {self.__x}/{self.y} -
            {self.__width} {self.height}"""

    def update(self, *args, **kwargs):
        """
        This method recieves two arguments:
            1- list of arguments (non-keywarded) tuple
            2- list of argumenst (keywared) like dictionary
        It assigns the itmes of the args to the instances attribues
        of the rectangle, if args is None or is [] (empty), it uses
        the keywarded list instead
        """

        if args is not None and args != ():
            key = list(self.__dict__.keys())
            id_key = key[-1]
            key.insert(0, id_key)

            for idx, item in enumerate(args):
                self.__dict__[key[idx]] = item

        else:
            keys = list(self.__dict__.keys())
            for k, v in kwargs.items():
                # keys = list(self.__dict__.keys())
                match(k):
                    case 'width':
                        self.__dict__[keys[0]] = v
                    case 'height':
                        self.__dict__[keys[1]] = v
                    case 'x':
                        self.__dict__[keys[2]] = v
                    case 'y':
                        self.__dict__[keys[3]] = v
                    case 'id':
                        self.__dict__[keys[4]] = v

    def to_dictionary(self):
        """
        This method returns a dictionary that represent
        the object (instances of the rectangle class)
        attributes
        """

        current_dict = self.__dict__
        from_keys = list(self.__dict__.keys())
        to_keys = ['id', 'width', 'height', 'x', 'y']
        new_dict = {}

        for idx, item in enumerate(to_keys):
            for k, v in self.__dict__.items():
                if item in k:
                    new_dict[item] = v
        return new_dict

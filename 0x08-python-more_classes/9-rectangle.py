#!/usr/bin/python3

""" This module creates an ampty class that models a rectangle """


class Rectangle:
    """ This class Models a simple rectangle """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with
        height == width == size """
        if size >=0 and isinstance(size, int):
            return cls(size, size)
        return cls(0,0)

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    def __repr__(self):
        """ This function returns a string """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __str__(self):
        """ This magic function return a string """
        my_str = ""
        for w in range(0, self.height):
            for h in range(0, self.width):
                my_str += str(self.print_symbol)
            if self.height - 1 != w:
                my_str += "\n"
            else:
                pass
        return my_str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ This is a static method that calculates and print the
        biggest recatngle based on area size """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.width * rect_1.height > rect_2.width * rect_2.height:
            return rect_1
        elif rect_1.width * rect_1.height < rect_2.width * rect_2.height:
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        """ a proprety to return the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ a property to first check the width attribue if its not < 0 and
        that it is an integer """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ a proprety to return the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ a property to first check the height attribue if its not < 0 and
        that it is an integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This is a public instance method that
        calclates and return the area of the
        rectangle """
        return self.height * self.width

    def perimeter(self):
        """ This is a public instance method
        that calculates and return the perimeter
        of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

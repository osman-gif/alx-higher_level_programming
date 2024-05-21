#!/usr/bin/python3
""" creates a class Square that defines a square """


class Square:

    """ This class is to model a square """

    def area(self):
        """ Returns the current squared area """

        return self._size ** 2


    @property
    def size(self):

        """ gets the size of the current area """
        return self._size

    @size.setter
    def size(self, __size):
        """ sets the current size """

        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self._size = __size



    @property
    def position(self):
        """ Returns the position private instance """

        return self._position

    @position.setter
    def position(self, __position):
        """ Sets the position private instance """
        if type(__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if __position[0] < 0 or __position[1] < 0:
                raise TypeError(""" position must be a tuple
                        of 2 positive integers """)
        self._position = __position
    
    def my_print(self):
        """ prints in stdout the square with the character # """

        if self._size == 0:
            print("")
        if self._position[1] != 0:
            print("")

        for i in range(0, self._size):
            for i in range(0, self._position[0]):
                if self._position[1] > 0:
                    print("", end="")
                print(" ", end="")

            for j in range(0, self._size):
                print("#", end="")
            print("")

    def __init__(self, __size=0, __position=(0, 0)):
        """ Initilaizes an instance of square class """

        self._size = __size
        self._position = __position
    def __str__(self):
        self._size = __size

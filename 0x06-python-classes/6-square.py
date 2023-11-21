#!/usr/bin/python3
class Square:
    """ This class is to model a square """
    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print("")
        if self.position[1] != 0:
            print("")

        for i in range(0, self._size):
            for i in range(0, self.position[0]):
                if self.position[1] > 0:
                    print("", end="")
                print(" ", end="")

            for j in range(0, self._size):
                print("#", end="")
            print("")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, _size):
        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._size = _size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, _position):
        if type(_position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if _position[0] < 0 or _position[1] < 0:
                raise TypeError(""" position must be a tuple
                        of 2 positive integers """)
        self._position = _position

    def __init__(self, _size=0, _position=(0, 0)):
        self._size = _size
        self._position = _position

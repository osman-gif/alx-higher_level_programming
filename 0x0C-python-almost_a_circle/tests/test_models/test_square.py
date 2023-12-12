#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(2)
        self.s2 = Square(2,2,2)

    def test_init__(self):
        with self.assertRaises(ValueError):
            s3 = Square(0)
        with self.assertRaises(TypeError):
            s3 = Square()
        with self.assertRaises(TypeError):
            s3 = Square(1,1,1,1,1)
        with self.assertRaises(ValueError):
            s3 = Square(-2)

    def test_to_dictionary(self):

        self.assertEqual(self.s1.to_dictionary(),{'id': 5, 'size': 2, 'x': 0, 'y': 0})
        self.assertAlmostEqual(self.s2.to_dictionary(),{'id': 6, 'size': 2, 'x': 2, 'y': 2})

    def test_str__(self):

        self.assertEqual(self.s2.__str__(),'[Square] (4) 2/2 - 2')

    def test_update(self):
        kwargs = {"x":10, "y":20}
        args = (1,1,1,1)

        self.s1.update(**kwargs)
        self.assertEqual(str(self.s1), '[Square] (7) 10/20 - 2')

        self.s1.update(*args)
        self.assertEqual(str(self.s1), '[Square] (1) 1/1 - 1')
        self.assertEqual(str(self.s1), '[Square] (1) 1/1 - 1')
        
        self.s1.update()
        self.assertEqual(str(self.s1), '[Square] (1) 1/1 - 1')

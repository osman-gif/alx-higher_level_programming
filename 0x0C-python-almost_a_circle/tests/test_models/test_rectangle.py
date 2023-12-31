#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(2, 2, 2, 2)
        self.kwargs = {"x": 10, "y": 20}

    def test_init__(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_area(self):
        self.assertEqual(self.r1.area(), 4)

    def test_str(self):
        self.assertEqual(
                str(self.r1), '[Rectangle] (3) 2/2 -\n            2 2')

    def test_update(self):
        self.r1.update(**self.kwargs)
        self.assertEqual(
                str(self.r1), '[Rectangle] (5) 10/20 -\n            2 2')

    def test_to_dictionary(self):
        self.r1.to_dictionary()
        self.assertEqual(
                str(self.r1.to_dictionary()
                    ), "{'id': 4, 'width': 2, 'height': 2, 'x': 2, 'y': 2}")

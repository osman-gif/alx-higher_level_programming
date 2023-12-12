#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([[]]), "[[]]")
        self.assertEqual(Base.to_json_string({}), "[]")
        self.assertEqual(Base.to_json_string(()), "[]")
        self.assertEqual(Base.to_json_string(""), "[]")
        self.assertEqual(Base.to_json_string(Base.from_json_string("null")), "[]")
        self.assertEqual(Base.to_json_string(Base.__name__), '"Base"')

        with self.assertRaises(TypeError):
            Base.to_json_string(Base.__dict__.items())
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string(3,3)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('{"key":"value"}'),{'key': 'value'})
        self.assertEqual(Base.from_json_string('["key","value"]'),['key', 'value'])
        self.assertEqual(Base.from_json_string(Base.to_json_string(None)), [])
        self.assertEqual(Base.from_json_string('[{"key":"value"},{"key":"value"}]'), [{'key': 'value'}, {'key': 'value'}])
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([])

    def test_save_to_file(self):

        self.assertFalse(Base.save_to_file([Rectangle(1,2), Rectangle(3,4)]))
        self.assertFalse(Base.save_to_file([Square(1,2,3), Rectangle(2,3)]))

        with self.assertRaises(TypeError):
            Base.save_to_file()
        with self.assertRaises(AttributeError):
            Base.save_to_file([3,4,4])
        with self.assertRaises(TypeError):
            Base.save_to_file(4)
        with self.assertRaises(NameError):
            Base.save_to_file(name)

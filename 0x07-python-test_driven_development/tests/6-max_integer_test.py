#!/usr/bin/python3
"""
Testing the max_integer function
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxList(unittest.TestCase):

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([2,3,5,1]), 5)
        self.assertEqual(max_integer([2,3.3,4,5.5]), 5.5)
        self.assertAlmostEqual(max_integer([-2,-3,-5,-1]), -1)

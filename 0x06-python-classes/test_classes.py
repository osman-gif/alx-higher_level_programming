import unittest
from square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.squ = Square(7, (0,0))

    def test_area(self):
        self.assertEqual(self.squ.area(), 49)
    
    def test_size(self):
        self.assertEqual(self.squ.size(5), 55)

if __name__ == '__main__':
    unittest.main()

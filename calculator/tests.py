import unittest

class TestCalculator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1 + 1, 2)
    
    def test_2(self):
        self.assertEqual(2 * 3, 6)
    
    def test_3(self):
        self.assertEqual(10 - 5, 5)
    
    def test_4(self):
        self.assertEqual(20 / 4, 5)
    
    def test_5(self):
        self.assertEqual(3 ** 2, 9)
    
    def test_6(self):
        self.assertEqual(10 % 3, 1)
    
    def test_7(self):
        self.assertEqual(abs(-5), 5)
    
    def test_8(self):
        self.assertEqual(max(1, 2, 3), 3)
    
    def test_9(self):
        self.assertEqual(min(1, 2, 3), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
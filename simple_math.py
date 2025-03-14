import unittest

class SimpleMath:
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x

class TestSimpleMath(unittest.TestCase):
    def setUp(self):
        self.math = SimpleMath()

    def test_square(self):
        # Тестируем метод square
        self.assertEqual(self.math.square(2), 4)
        self.assertEqual(self.math.square(0), 0)
        self.assertEqual(self.math.square(-3), 9)

    def test_cube(self):
        # Тестируем метод cube
        self.assertEqual(self.math.cube(3), 27)
        self.assertEqual(self.math.cube(0), 0)
        self.assertEqual(self.math.cube(-3), -27)

if __name__ == '__main__':
    unittest.main()
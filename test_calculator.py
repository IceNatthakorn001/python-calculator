import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-6, -2), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(5, -1), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(-5, 5), -25)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(-25, -5), 5)
        self.assertEqual(self.calc.divide(25, 0), "cannot divide by zero")
        self.assertEqual(self.calc.divide(0, 32), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(99, -3), 0)
        self.assertEqual(self.calc.modulo(-12, -5), -2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
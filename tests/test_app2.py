import unittest
from backend import multiply


class TestApp2(unittest.TestCase):
    def test_multiply(self):
        result1 = multiply(2, 3)
        self.assertEqual(result1, 6)

        result2 = multiply(-2, -5)
        self.assertEqual(result2, 10)
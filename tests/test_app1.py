import unittest
from backend import add


class TestApp1(unittest.TestCase):
    def test_add(self):
        result = add(1, 3)
        self.assertEqual(result, 4)

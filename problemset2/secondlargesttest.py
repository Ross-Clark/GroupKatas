import secondlargest
import unittest

class Test2ndLargest(unittest.TestCase):
    def test_number_array(self):
        self.assertEqual(secondlargest.find([1, 2, 3]), 2)

    def test_equal_numbers(self):
        self.assertEqual(secondlargest.find([1, 1, 1]), None)

    def test_numbers_and_chars(self):
        self.assertEqual(secondlargest.find([1, "a", 2, 1, "b", 3]), 2)

    def test_empty(self):
        self.assertEqual(secondlargest.find([]), None)

    def test_chars(self):
        self.assertEqual(secondlargest.find(["a", "b", "c"]), None)

    def test_minus_numbers(self):
        self.assertEqual(secondlargest.find([-2, -5, 10]), -2)

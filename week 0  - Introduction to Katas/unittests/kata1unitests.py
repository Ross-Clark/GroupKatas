import unittest

from katasfirstone import kata1

class katas1test(unittest.TestCase):
    def test_return_two(self):
        list = [2,1,1]
        response = kata1(list)
        self.assertEqual(response, 2)

    def test_return_null(self):
        list = [2, 2, 2]
        response = kata1(list)
        self.assertEqual(response, None)



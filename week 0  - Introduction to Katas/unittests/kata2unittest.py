import unittest

from katasecondone import kata2

class katas1test(unittest.TestCase):
    def test_return_two(self):
        list = [2,1,1]
        response = kata2(list)
        self.assertEqual(response, True)

    def test_return_null(self):
        list = [2, 2, 2]
        response = kata2(list)
        self.assertEqual(response, None)

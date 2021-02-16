import unittest

from kata1 import kata_1


class TestKata1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(kata_1([1, 3, 3]), 1)

    def test_2(self):
        self.assertEqual(kata_1([1, 2, 2]), 1)

    def test_3(self):
        self.assertEqual(kata_1([1, 2, 2, 0, 0]), 1)

    def test_4(self):
        self.assertEqual(kata_1([2, 5, 5]), 2)

    def test_5(self):
        self.assertEqual(kata_1([66, 66, 0, 3, 3]), 0)

    def test_6(self):
        self.assertEqual(kata_1([2, 2, 34, 34, -99]), -99)

    def test_7(self):
        self.assertEqual(kata_1([2, 2, 34, 34, -99]), -99)

    def test_8(self):
        self.assertEqual(kata_1([-2, 7, -67, -67, -2]), 7)

    def test_9(self):
        self.assertEqual(kata_1([-2, 34, 21, 99, 0, -2, -67, 0, 45, -67, 21, 34, 99]), 45)

if __name__ == '__main__':
    unittest.main()
import unittest

from kata2 import kata_2


class TestKata1(unittest.TestCase):

    def test_1(self):
        self.assertTrue(kata_2([1, 3, 3]))

    def test_2(self):
        self.assertFalse(kata_2([1, 2, 3]))

    def test_3(self):
        self.assertTrue(kata_2([0, 0]))

    def test_4(self):
        self.assertTrue(kata_2([-2, -5, -5]))

    def test_5(self):
        self.assertFalse(kata_2([-66, 56, -10]))

    def test_6(self):
        self.assertFalse(kata_2([1, 4, 5, 34, 7345, 234, 66534, 343]))

    def test_7(self):
        self.assertTrue(kata_2([-2, -7, -64, -64, -2, -2, -7, -64, -64, -2, -2, -7, -64, -64, -2]))

    def test_8(self):
        self.assertTrue(kata_2([-2, 34, 21, 99, 0, -2, -67, 0, 45, -67, 21, 34, 99]))

    def test_9(self):
        self.assertFalse(kata_2([1]))


if __name__ == '__main__':
    unittest.main()

import unittest

import second_largest as sut


class TestSecondLargest(unittest.TestCase):
    def test_second_largest_returns_the_second_largest(self):
        # Arrange
        input_list = [1, 2, 3]
        expected = 2
        # Act
        actual = sut.second_largest(input_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_second_largest_returns_None_if_no_second_largest_int(self):
        # Arrange
        input_list = [1, 1, 1, 1, 1]
        expected = None
        # Act
        actual = sut.second_largest(input_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_second_largest_returns_the_second_largest_2(self):
        # Arrange
        input_list = [1, "b", 1, 2, "c", 1]
        expected = None
        # Act
        actual = sut.second_largest(input_list)
        # Assert
        self.assertEqual(expected, actual)

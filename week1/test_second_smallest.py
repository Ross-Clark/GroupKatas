import unittest

import second_smallest as sut


class TestSecondsmallest(unittest.TestCase):
    def test_second_smallest_returns_the_second_smallest(self):
        # Arrange
        input_list = [1, 2, 3]
        expected = 2
        # Act
        actual = sut.second_smallest(input_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_second_smallest_returns_None_if_no_second_smallest_int(self):
        # Arrange
        input_list = [1, 1, 1, 1, 1]
        expected = None
        # Act
        actual = sut.second_smallest(input_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_second_smallest_returns_the_second_smallest_2(self):
        # Arrange
        input_list = [1, "b", 1, 2, "c", 1]
        expected = None
        # Act
        actual = sut.second_smallest(input_list)
        # Assert
        self.assertEqual(expected, actual)

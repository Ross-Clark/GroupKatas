import unittest
import week0
from parameterized import parameterized


class TestWeek0(unittest.TestCase):
    @parameterized.expand([
        ([3, 3, 1, 3, 3, 4, 4], 1),
        ([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 7),
        ([-2, 7, -67, -67, -2], 7),
        ([-2, 34, 21, 99, 0, -2, -67, 0, 45, -67, 21, 34, 99], 45)
    ])
    def test_problem_1(self, input_list, expected):
        # Arrange/Act
        result = week0.problem_1(input_list)

        # Assert
        self.assertEquals(expected, result)

    @parameterized.expand([
        ([1, 1, 6, 8, 3, 8], True),
        ([1, 6, 9, 4, 2], False)
    ])
    def test_problem_2(self, input_list, expected):
        # Arrange/Act
        result = week0.problem_2(input_list)
        # Assert
        self.assertEquals(expected, result)

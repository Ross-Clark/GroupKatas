import unittest

import valid_anagram as sut


class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram_returns_true(self):
        # Arrange
        s = "binary"
        t = "brainy"
        expected = True
        # Act
        actual = sut.valid_anagram(s, t)
        # Assert
        self.assertEqual(expected, actual)

    def test_invalid_anagram_returns_false(self):
        # Arrange
        s = "rat"
        t = "car"
        expected = False
        # Act
        actual = sut.valid_anagram(s, t)
        # Assert
        self.assertEqual(expected, actual)
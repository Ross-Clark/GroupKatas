import validanagram
import unittest

class TestValidAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(validanagram.determine("binary", "brainy"))

    def test_not_anagram(self):
        self.assertFalse(validanagram.determine("rat", "car"))

    def test_not_quite_anagram(self):
        self.assertFalse(validanagram.determine("aaa", "aaaa"))

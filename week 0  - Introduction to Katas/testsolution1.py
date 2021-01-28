import unittest
from solution1 import findSingleNumber

class TestFindSingleNumber(unittest.TestCase):

    def test_happy_path(self):
        # Arrange
        input = [1, 2, 2, 3, 3, 4, 4]

        # Act
        answer = findSingleNumber(input)

        # Assert
        self.assertEqual(answer, 1)
        

if __name__ == '__main__':
    unittest.main()

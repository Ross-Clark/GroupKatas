import unittest
from solution2 import findDuplicates

class TestFindDuplicates(unittest.TestCase):

    def test_happy_path_true(self):
        # Arrange
        input = [1, 2, 1, 3, 4]

        # Act
        answer = findDuplicates(input)

        # Assert
        self.assertTrue(answer)

    
    def test_happy_path_false(self):
        # Arrange
        input = [1, 2, 5, 3, 4]

        # Act
        answer = findDuplicates(input)

        # Assert
        self.assertFalse(answer)
        

if __name__ == '__main__':
    unittest.main()

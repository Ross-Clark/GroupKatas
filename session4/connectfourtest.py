import unittest
import connectfour

class connectfourtest(unittest.TestCase):
    def test_missing_row(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','Y','Y']]),
                                            1)
    def test_missing_slot(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','Y','Y'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            1)
    def test_too_many_rows(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','Y','Y'],
                                            ['-','-','-','Y','R','Y','Y'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            1)
    def test_too_many_slots(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','Y','Y','-'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            1)

    def test_horizontal_red_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','Y','Y'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            'R')
    def test_horizontal_yellow_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','R','-','-','R'],
                                            ['-','-','-','Y','Y','Y','Y'],
                                            ['-','-','-','Y','R','R','Y'],
                                            ['-','-','-','Y','R','R','R']]),
                                            'Y')
        
    def test_vertical_red_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','R','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','R','Y'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            'R')
    def test_vertical_yellow_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','Y','R','-','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','R','Y'],
                                            ['-','-','Y','Y','R','R','R']]),
                                            'Y')

    def test_diagonal_red_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','Y','R','R'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','R','Y'],
                                            ['-','-','Y','R','R','Y','R']]),
                                            'R')
    
    def test_diagonal_yellow_win(self):
        self.assertEqual(connectfour.connectFour([['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','-','-','-'],
                                            ['-','-','-','-','R','Y','-'],
                                            ['-','-','-','Y','Y','R','Y'],
                                            ['-','-','-','Y','R','R','Y'],
                                            ['-','-','Y','R','R','Y','R']]),
                                            'Y')

    def test_draw(self):
        self.assertEqual(connectfour.connectFour([['Y','R','Y','R','Y','R','Y'],
                                                  ['Y','R','Y','R','Y','R','Y'],
                                                  ['R','Y','R','Y','R','Y','R'],
                                                  ['R','Y','R','Y','Y','R','Y'],
                                                  ['Y','R','Y','R','Y','R','Y'],
                                                  ['Y','R','Y','R','R','Y','R']]),
                                                  'draw')

    def test_in_progress(self):
        self.assertEqual(connectfour.connectFour([['-','-','Y','R','Y','R','Y'],
                                                  ['Y','R','Y','R','Y','R','Y'],
                                                  ['R','Y','R','Y','R','Y','R'],
                                                  ['R','Y','R','Y','Y','R','Y'],
                                                  ['Y','R','Y','R','Y','R','Y'],
                                                  ['Y','R','Y','R','R','Y','R']]),
                                                  'in progress')
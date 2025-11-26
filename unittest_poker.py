import unittest
from poker import *

class TestPoker(unittest.TestCase):
    def test_has_pair(self):
        cards = [0, 1, 13, 14, 26]
        self.assertEqual(has_pair(cards), True, "Es sollte ein Paar gefunden werden.")
        cards = [0, 1, 2, 3, 4]  # Kein Paar
        self.assertEqual(has_pair(cards), False, "Es sollte kein Paar gefunden werden.")

    def has_two_pair(self):
        cards = [0, 1, 13, 14, 26]
        self.assertEqual(has_two_pair(cards), True, "Es sollten zwei Paare gefunden werden.")
        cards = [0, 1, 13, 2, 3]
        self.assertEqual(has_two_pair(cards), False, "Es sollten nicht zwei Paare gefunden werden.")

    def has_full_house(self):
        cards = [1,1,1,13,13]
        self.assertEqual(has_full_house(cards), True, "Es sollte ein full house gefunden werden.")
        cards = [1,1,13,13,15]
        self.assertEqual(has_full_house(cards), False, "Es sollte kein full house gefunden werden.")

    def is_royal_flush(self):
        cards = [0, 9, 10, 11, 12]
        self.assertEqual(is_royal_flush(cards), True, "Es sollte eine royal flush gefunden werden.")
        cards = [8,9,10,11,12]
        self.assertEqual(is_royal_flush(cards), False, "Es sollte keine royal flush gefunden werden.")

if __name__ == '__main__':
    unittest.main()
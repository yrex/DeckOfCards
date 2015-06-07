import unittest
from DeckOfCards import Suit


class TestSuit(unittest.TestCase):

    def test_Suit_instance(self):
        s = Suit('Diamond', 2)
        self.assertIsInstance(s, Suit)

    def test_Suit_name(self):
        s = Suit('Diamond', 2)
        self.assertEqual(s.name, 'Diamond')

    def test_Suit_rank(self):
        s = Suit('Diamond', 2)
        self.assertEqual(s.rank, 2)

    def test_Suit_lt1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertTrue(s1 < s2)

    def test_Suit_lt2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 < s2)

    def test_Suit_lt3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 < s2)

    def test_Suit_le1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertTrue(s1 <= s2)

    def test_Suit_le2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 <= s2)

    def test_Suit_le3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 <= s2)

    def test_Suit_eq1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertFalse(s1 == s2)

    def test_Suit_eq2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 == s2)

    def test_Suit_eq3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 == s2)

    def test_Suit_ne1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertTrue(s1 != s2)

    def test_Suit_nq2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 != s2)

    def test_Suit_nq3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 != s2)

    def test_Suit_gt1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertFalse(s1 > s2)

    def test_Suit_gt2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 > s2)

    def test_Suit_gt3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertFalse(s1 > s2)

    def test_Suit_ge1(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 3)
        self.assertFalse(s1 >= s2)

    def test_Suit_ge2(self):
        s1 = Suit('Diamond', 3)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 >= s2)

    def test_Suit_ge3(self):
        s1 = Suit('Diamond', 2)
        s2 = Suit('Heart', 2)
        self.assertTrue(s1 >= s2)

if __name__ == '__main__':
    unittest.main()

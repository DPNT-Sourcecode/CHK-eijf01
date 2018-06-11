import unittest
from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("AB"), 80)

    def test_checkout_clean_input(self):
        self.assertEqual(checkout(" A   B "), 80)

    def test_checkout_multi(self):
        self.assertEqual(checkout("A B A"), 130)

    def test_checkout_offer(self):
        self.assertEqual(checkout("A A B B A"), 175)

    def test_checkout_illegal(self):
        self.assertEqual(checkout("pandas"), -1)

    def test_checkout_illegal2(self):
        self.assertEqual(checkout("A E"), -1)


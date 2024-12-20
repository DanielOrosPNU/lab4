import unittest
import lab4


class ReverseTest(unittest.TestCase):
    def test_firsttest(self):
        word = lab4.rev_str("babel")
        self.assertEqual(word, "lebab")

    def test_secondtest(self):
        word = lab4.rev_str("babel land")
        self.assertEqual(word, "lebab dnal")

    def test_thirdtest(self):
        word = lab4.rev_str(" ")
        self.assertEqual(word, '')

    def test_fourthtest(self):
        word = lab4.rev_str("babe1l")
        self.assertEqual(word, "leba1b")

    def test_fifthtest(self):
        with self.assertRaises(TypeError) as context:
            lab4.rev_str(123)
        self.assertTrue("Input must be a string" in str(context.exception))

import unittest
from part2 import *

class TestFunctions(unittest.TestCase):

    def test_compute_standard_deviation(self):
        self.assertAlmostEqual(compute_standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertEqual(compute_standard_deviation([]), None)
        self.assertAlmostEqual(compute_standard_deviation([10, 10, 10]), 0)

    def test_find_second_largest(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_largest([1, 1, 1]), None)
        self.assertEqual(find_second_largest([5, 5, 4, 4]), 4)
        self.assertEqual(find_second_largest([-1, -2, -3, -4]), -2)

    def test_character_frequency_per_word(self):
        self.assertEqual(character_frequency_per_word("hello world"),
                         {'hello': {'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'world': {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}})
        self.assertEqual(character_frequency_per_word("abc abc"), {'abc': {'a': 1, 'b': 1, 'c': 1}})
        self.assertEqual(character_frequency_per_word("a a a"), {'a': {'a': 1}})


    def test_longest_word_in_sentence(self):
        self.assertEqual(longest_word_in_sentence("The quick brown fox jumped"), "jumped")
        self.assertEqual(longest_word_in_sentence("Hello world"), "Hello")
        self.assertEqual(longest_word_in_sentence("Quick"), "Quick")

        self.assertEqual(longest_word_in_sentence("A B C D E F G H I J K L M N O P"), "P")

if __name__ == '__main__':
    unittest.main()

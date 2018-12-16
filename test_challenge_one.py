import unittest
from challenge import get_numbers

# It would be better to use pytest but it's not yet in standard library.
# I use python sets because the elements are unique and a set is always ordered.
# It could be easily converted to python lists.


class TestGetNumbers(unittest.TestCase):

    def test_base_cases(self):
        data = (
            ('', set()),
            ('abcd', set()),
            ('100', {100}),
            ('A56B455VB23GTY23J', {23, 56, 455}),
            ('ABCDEF23', {23}),
            ('21ABDEF', {21}),
            ('23ABasdBD21', {21, 23}),
            ('AB0DE23BAD1', {0, 1, 23}),
            ('AB0000DE', {0}),
            ('AB0001DE', {1}),
        )
        for text, expected in data:
            self.assertEqual(get_numbers(text), expected)

    def test_huge_data(self):
        length = 1000000
        text = '{}23{}21'.format('a' * length, 'b' * length)
        self.assertEqual(get_numbers(text), {21, 23})


if __name__ == '__main__':
    unittest.main()

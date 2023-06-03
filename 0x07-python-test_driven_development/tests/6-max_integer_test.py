#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered(self):
        """ check the max int of an ordered list """

        ordered = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered(self):
        """check for max integer in an unordered list"""
        unordered = [2, 5, 7, 8, 14, 70, 64, 45]
        self.assertEqual(max_integer(unordered), 70)

    def test_reversed(self):
        """check for max in a reversed list """
        reversed = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(reversed), 5)

    def test_negative(self):
        """check for max within negative numbers """
        negative = [-1, -3, -6, -4]
        self.assertEqual(max_integer(negative), -1)

    def test_mixed(self):
        """check for max integer within negative and positive numbers"""
        mixed = [-2, 5, 3, -4, 5]
        self.assertEqual(max_integer(mixed), 5)

    def test_double(self):
        """check for max integer within repeated numbers"""
        double = [2, 4, 2, 4, 6, 5, -5, -5, 6]
        self.assertEqual(max_integer(double), 6)

    def test_empty(self):
        """check for max in an empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_float(self):
        """check for max within a floating element """
        float_list = [4.1, 5.0, 5.6, 10.1, 8.3]
        self.assertEqual(max_integer(float_list), 10.1)

    def test_float_int(self):
        """check for max within float and int"""
        numbers = [1, 4, 5.3, 5, 6, 3.5]
        self.assertEqual(max_integer(numbers), 6)

    def test_strings(self):
        """check for max within strings """
        names = ['faith', 'john', 'bob', 'julien']
        self.assertEqual(max_integer(names), 'julien')

    def test_empty_string(self):
        """test an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 50]), 50)

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_negatives(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-10, -5, -1, -7]), -1)

    def test_mixed_int_float(self):
        """Test a list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_strings(self):
        """Test a list of strings (lexicographical order)"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_list_of_one_string(self):
        """Test a list with one string"""
        self.assertEqual(max_integer(["single"]), "single")

    def test_list_with_duplicates(self):
        """Test a list with duplicate max values"""
        self.assertEqual(max_integer([5, 1, 5, 3]), 5)

if __name__ == "__main__":
    unittest.main()

""" 
@Program: test
@Author: Donald Osgood
@Last Date: 2023-11-28 22:23:30
@Purpose:Donald Osgood
"""
import unittest
from fractions import Fraction
from my_sum import *
from utils.conversions import truncate_to_decimal


class TestSum(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): unittest ibject
    """    
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def neg_test_truncate_to_decimal(self):
        """
        Negative test decimalconversion
        """
        result = truncate_to_decimal("two")
        self.assertEqual(result, 2)
        with self.assertRaises(TypeError):
            print(TypeError)
            
    def pos_test_truncate_to_decimal(self):
        """
        Positive test decimalconversion
        """
        result = truncate_to_decimal(2.0)
        self.assertEqual(result, 2)
        with self.assertRaises(TypeError):
            print(TypeError)

    def test_bad_type(self):
        """
        Testing bad type data
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
            print(result)


if __name__ == "__main__":
    unittest.main()

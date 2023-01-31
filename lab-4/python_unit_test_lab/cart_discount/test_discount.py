import unittest 
from unittest import TestCase
from price_discount import discount 

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_less_than_three_prices(self):
        prices = [10, 2]
        self.assertIsNone(discount(prices))

    def test_prices_not_negative(self):
        prices = [-9, 10, 11, 12]
        expected_lowest_number = 10
        self.assertEqual(expected_lowest_number, discount(prices))

    def test_all_prices_the_same_still_chooses_value(self):
        prices = [10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_empty_list(self):
        prices = []
        self.assertIsNone(discount(prices))

    def test_item_prices_is_list(self):
        prices = {}
        self.assertIsNone(discount(prices))

if __name__ == '__main__':
    unittest.main()
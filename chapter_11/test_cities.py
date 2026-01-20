import unittest
from cities import city_country

class CitiesTest(unittest.TestCase):
    """tests if the city_country function works properly"""
    def test_city_country(self):
        formatted_country = city_country('mexico city', 'mexico')
        self.assertEqual(formatted_country, 'Mexico City, Mexico')

    def test_city_country_population(self):
        formatted_country = city_country('mexico city', 'mexico', 120)
        self.assertEqual(formatted_country, 'Mexico City, Mexico - population: 120')

unittest.main()
#!/usr/bin/python3
"""
Test suite for City class
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Tests for the City class
    """

    def test_create_city_instance(self):
        """
        Test creating an instance of City class
        """
        city = City()
        self.assertIsInstance(city, City)
        
    def test_city_attributes(self):
        """
        Test setting city attributes
        """
        city = City()
        city.name = "New York"
        city.state = "New York"
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state, "New York")

    def test_city_methods(self):
        """
        Test methods of the City class
        """
        # Implement test cases for specific methods of the City class
        pass

if __name__ == '__main__':
    unittest.main()


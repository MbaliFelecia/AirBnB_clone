#!/usr/bin/python3
"""
Test suite for Place class
"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Tests for the Place class
    """

    def test_create_place_instance(self):
        """
        Test creating an instance of Place class
        """
        place = Place()
        self.assertIsInstance(place, Place)
        
    def test_place_attributes(self):
        """
        Test setting place attributes
        """
        place = Place()
        place.name = "Cozy Apartment"
        place.price_per_night = 100
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.price_per_night, 100)

    def test_place_methods(self):
        """
        Test methods of the Place class
        """
        # Implement test cases for specific methods of the Place class
        pass

    def test_place_availability(self):
        """
        Test place availability logic
        """
        place = Place()
        place.available = True
        self.assertTrue(place.available)
        place.available = False
        self.assertFalse(place.available)

if __name__ == '__main__':
    unittest.main()


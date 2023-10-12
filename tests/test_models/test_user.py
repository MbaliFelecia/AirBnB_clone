#!/usr/bin/python3
"""
Test suite for User class
"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Tests for User class
    """

    def test_user_creation(self):
        """
        Test creating a User instance
        """
        user = User()
        self.assertIsInstance(user, User)
        
    def test_user_attributes(self):
        """
        Test setting user attributes
        """
        user = User()
        user.username = "john_doe"
        user.email = "john.doe@example.com"
        
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john.doe@example.com")

if __name__ == '__main__':
    unittest.main()


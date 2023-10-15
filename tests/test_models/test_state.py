#!/usr/bin/python3
"""
Test suite for State class
"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Tests for State class
    """

    def test_state_creation(self):
        """
        Test creating a State instance
        """
        state = State()
        self.assertIsInstance(state, State)
        
    def test_state_attributes(self):
        """
        Test setting state attributes
        """
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")
        state.name = "California"  # Updated state name
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()


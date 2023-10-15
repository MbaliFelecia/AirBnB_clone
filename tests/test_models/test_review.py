#!/usr/bin/python3
"""
Test suite for Review class
"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Tests for Review class
    """

    def test_review_creation(self):
        """
        Test creating a Review instance
        """
        review = Review()
        self.assertIsInstance(review, Review)
        
    def test_review_attributes(self):
        """
        Test setting review attributes
        """
        review = Review()
        review.user_id = "user123"
        review.place_id = "place456"
        review.text = "Great experience!"
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.place_id, "place456")
        self.assertEqual(review.text, "Great experience!")

    def test_review_rating(self):
        """
        Test review rating logic
        """
        review = Review()
        review.rating = 5
        self.assertEqual(review.rating, 5)
        review.rating = -1  # Invalid rating, should be handled in your Review class
        self.assertNotEqual(review.rating, -1)

if __name__ == '__main__':
    unittest.main()


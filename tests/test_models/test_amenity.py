```python
#!/usr/bin/python3
"""
Unit tests for amenities module
"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """

    def test_name_attribute(self):
        """
        Test if the Amenity instance has name attribute
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIsInstance(amenity.name, str)

    def test_created_at_attribute(self):
        """
        Test if the Amenity instance has created_at attribute
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_attribute(self):
        """
        Test if the Amenity instance has updated_at attribute
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_string_representation(self):
        """
        Test the string representation of Amenity
        """
        amenity = Amenity()
        string_repr = str(amenity)
        self.assertIn("[Amenity]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'name':", string_repr)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Amenity class
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("name", amenity_dict)

if __name__ == '__main__':
    unittest.main()
```

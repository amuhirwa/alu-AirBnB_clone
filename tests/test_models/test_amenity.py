#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Class to test the amenity class."""

    def __init__(self, *args, **kwargs):
        """Initialize TestAmenity instance."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.name), str)

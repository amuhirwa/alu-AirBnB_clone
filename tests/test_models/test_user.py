#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class to test the User class."""

    def __init__(self, *args, **kwargs):
        """Initialize TestUser instance."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email(self):
        new = self.value()
        self.assertEqual(type(new.email), str)
    
    def test_password(self):
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.first_name), str)
        self.assertEqual(type(new.last_name), str)

if __name__ == '__main__':
    unittest.main()

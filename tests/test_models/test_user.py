#!/usr/bin/python3
"""Module for Users model test cases."""
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class test_User(TestBasemodel):
    """Users model test cases."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Evaluate type of first_name."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Evaluate type of last_name."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Evaluate type of email."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Evaluate type of password."""
        new = self.value()
        self.assertEqual(type(new.password), str)

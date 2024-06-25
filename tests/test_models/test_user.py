#!/usr/bin/python3
"""Module for Users model test cases."""
import os
import unittest

from models.user import User
from tests.test_models.test_base_model import TestBasemodel


class TestUser(TestBasemodel):
    """Represents the tests for the User model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests the type of first_name."""
        new = self.value()
        self.assertEqual(
            type(new.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None),
            "First name should be str if not using DB storage"
        )

    def test_last_name(self):
        """Tests the type of last_name."""
        new = self.value()
        self.assertEqual(
            type(new.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None),
            "Last name should be str if not using DB storage"
        )

    def test_email(self):
        """Tests the type of email."""
        new = self.value()
        self.assertEqual(
            type(new.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None),
            "Email should be str if not using DB storage"
        )

    def test_password(self):
        """Tests the type of password."""
        new = self.value()
        self.assertEqual(
            type(new.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None),
            "Password should be str if not using DB storage"
        )

    def test_init(self):
        """Test initialization of User model."""
        new = self.value()
        self.assertIsInstance(
            new,
            User,
            "Instance should be an instance of User"
        )

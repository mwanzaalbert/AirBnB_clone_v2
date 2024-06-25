#!/usr/bin/python3
"""Module of city database values test cases."""
import os
import unittest

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestCity(TestBasemodel):
    """Represents the tests for the City model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the type and default value of state_id."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsNone(new.state_id)

    def test_name(self):
        """Test the type and default value of name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsNone(new.name)

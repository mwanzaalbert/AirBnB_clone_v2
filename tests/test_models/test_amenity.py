#!/usr/bin/python3
"""Amenity test module."""
import os
import unittest

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBasemodel


class TestAmenity(TestBasemodel):
    """Represent the tests for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """Test the type and default value of name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsNone(new.name)

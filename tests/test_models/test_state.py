#!/usr/bin/python3
"""Module for state model test cases."""
import os
import unittest

from models.state import State
from tests.test_models.test_base_model import TestBasemodel


class TestState(TestBasemodel):
    """Represents the tests for the State model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests the type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Skip test for DB storage"
    )
    def test_name_file_storage(self):
        """Test name type for FileStorage."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str,
            "Name should be str for FileStorage"
        )

    def test_init(self):
        """Test initialization of State model."""
        new = self.value()
        self.assertIsInstance(
            new,
            State,
            "Instance should be an instance of State"
        )

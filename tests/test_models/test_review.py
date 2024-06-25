#!/usr/bin/python3
"""Module for place model test cases."""
import os
import unittest

from models.review import Review
from tests.test_models.test_base_model import TestBasemodel


class TestReview(TestBasemodel):
    """Represents the tests for the Review model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tests the type of place_id."""
        new = self.value()
        self.assertEqual(
            type(new.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_text(self):
        """Tests the type of text."""
        new = self.value()
        self.assertEqual(
            type(new.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Skip test for DB storage"
    )
    def test_place_id_file_storage(self):
        """Test place_id type for FileStorage."""
        new = self.value()
        self.assertEqual(
            type(new.place_id),
            str,
            "Place ID should be str for FileStorage"
        )

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Skip test for DB storage"
    )
    def test_user_id_file_storage(self):
        """Test user_id type for FileStorage."""
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str,
            "User ID should be str for FileStorage"
        )

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Skip test for DB storage"
    )
    def test_text_file_storage(self):
        """Test text type for FileStorage."""
        new = self.value()
        self.assertEqual(
            type(new.text),
            str,
            "Text should be str for FileStorage"
        )

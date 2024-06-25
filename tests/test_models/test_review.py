#!/usr/bin/python3
"""Module for place model test cases."""
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class test_review(TestBasemodel):
    """Review model test cases."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Evaluate type of place_id."""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Evaluate type of user_id."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Evaluate type of text."""
        new = self.value()
        self.assertEqual(type(new.text), str)

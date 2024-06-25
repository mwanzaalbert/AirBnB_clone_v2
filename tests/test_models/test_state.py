#!/usr/bin/python3
"""Module for state model test cases."""
from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class test_state(TestBasemodel):
    """State model test cases."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Evaluate type of name."""
        new = self.value()
        self.assertEqual(type(new.name), str)

#!/usr/bin/python3
"""Module of city database values test cases."""
from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class test_City(TestBasemodel):
    """City model test cases."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Evaluate the type of state_id."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests the type of name."""
        new = self.value()
        self.assertEqual(type(new.name), str)

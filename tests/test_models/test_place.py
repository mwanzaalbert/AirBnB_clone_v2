#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class test_Place(TestBasemodel):
    """Place model test cases."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Evaluate type of city id."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Evaluate type of user id."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Evaluate type of name."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Evaluate type of description of object."""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Evaluate type of number of rooms."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Evaluate type of number_bathrooms value."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Evaluate type of maxguest value."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Evaluate type of price_by_night."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Evaluate type of latitude."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Evaluate type of longitude."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Evaluate type of  """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

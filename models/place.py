#!/usr/bin/python3
"""Place Module for HBNB project."""
import os
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False, primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False, primary_key=True)
                          )


class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.
    Attributes_:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price by night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): The place's longitude.
        reviews (sqlalchemy relationship): The Place-Review relationship.
        amenities (sqlalchemy relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all associated Amenities.
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Get a list of all associated Reviews."""
        reviews_list = []

        for value in models.storage.all(Review).values():
            if value.place_id == self.id:
                reviews_list.append(value)
        return reviews_list

    @property
    def amenities(self):
        """Get associated Amenities."""
        amenity_list = []

        for value in models.storage.all(Amenity).values():
            if value.id in self.amenity_ids:
                amenity_list.append(value)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        """Add associated Amenities."""
        if type(value) is Amenity:
            if value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)

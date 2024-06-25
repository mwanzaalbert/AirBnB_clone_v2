#!/usr/bin/python3
"""State Module for HBNB project."""
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity in Place for the HBNB project.

    Attributes_:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False
                  ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

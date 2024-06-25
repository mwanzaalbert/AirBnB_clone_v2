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

    def __init__(self, *args, **kwargs):
        """Initialize an Amenity instance."""
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.name = kwargs.get('name', '')
            self.validate_name()

    def validate_name(self):
        """Validate the name attribute for non-DB storage."""
        if not self.name:
            raise ValueError("name attribute cannot be empty")

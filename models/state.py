#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class."""

    __tablename__ = 'states'

    # Define name attribute regardless of storage type
    name = Column(String(128), nullable=False)

    # Define cities relationship for database storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        # Define cities property for non-database storage
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals.

            to the current State.id.
            """
            from models import storage
            from models.city import City
            return [city for city in storage.all(
                City).values() if city.state_id == self.id]

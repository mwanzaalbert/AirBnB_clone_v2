#!/usr/bin/python3
"""City Module for HBNB project."""
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """Represent a city data set."""

    __tablename__ = 'cities'

    # Define state_id and name attributes regardless of storage type
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    # Define places relationship for database storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            'Place', backref='cities', cascade='all, delete'
        )

    def __init__(self, *args, **kwargs):
        """Initialize a City instance."""
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.state_id = kwargs.get('state_id', "")
            self.name = kwargs.get('name', "")
#             self.validate_attributes()

    def validate_attributes(self):
        """Validate the state_id and name attributes for non-DB storage."""
        if not self.state_id:
            raise ValueError("state_id attribute cannot be empty")
        if not self.name:
            raise ValueError("name attribute cannot be empty")

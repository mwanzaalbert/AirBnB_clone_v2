#!/usr/bin/python3
"""Review module for the HBNB project."""
import os
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Review class to store review information."""

    __tablename__ = 'reviews'

    # Database-specific attributes
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False
        )
        user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False
        )
        text = Column(
            String(1024), nullable=False
        )
    else:  # For non-database storage
        place_id = ''
        user_id = ''
        text = ''

    def __init__(self, *args, **kwargs):
        """Initialize the Review object."""
        super().__init__(*args, **kwargs)

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.place_id = kwargs.get('place_id', '')
            self.user_id = kwargs.get('user_id', '')
            self.text = kwargs.get('text', '')

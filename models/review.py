#!/usr/bin/python3
"""Review module for the HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class Review(BaseModel, Base):
    """
    A review object in the HBNB model.

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    Attributes_:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """

    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

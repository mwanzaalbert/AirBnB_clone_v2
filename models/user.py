#!/usr/bin/python3
"""Module defines a class User."""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """A user in the HBNB model.

    Inherits from SQLAlchemy Base and links to the MySQL table users.
    Attributes_:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """

    __tablename__ = "users"

    # Conditional attribute definitions based on the storage type
    email = Column(String(128), nullable=False) if os.getenv(
        'HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(String(128), nullable=False) if os.getenv(
        'HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(String(128), nullable=True) if os.getenv(
        'HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(String(128), nullable=True) if os.getenv(
        'HBNB_TYPE_STORAGE') == 'db' else ''

    # Define relationships based on the storage type
    places = relationship("Place", cascade="all, delete, delete-orphan",
                          backref="user") if os.getenv(
                              'HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship("Review", cascade="all, delete, delete-orphan",
                           backref="user") if os.getenv(
                               'HBNB_TYPE_STORAGE') == 'db' else None

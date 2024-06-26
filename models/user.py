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

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place", cascade="all, delete, delete-orphan", backref="user")
        reviews = relationship(
            "Review", cascade="all, delete, delete-orphan", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialize the User object."""
        super().__init__(*args, **kwargs)

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.email = kwargs.get('email', '')
            self.password = kwargs.get('password', '')
            self.first_name = kwargs.get('first_name', '')
            self.last_name = kwargs.get('last_name', '')

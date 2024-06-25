#!/usr/bin/python3
"""State Module for HBNB project."""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """A State representation in the HBNB model."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

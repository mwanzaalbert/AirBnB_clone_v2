#!/usr/bin/python3
"""City Module for HBNB project."""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """Representation of a city.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    Attributes_:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

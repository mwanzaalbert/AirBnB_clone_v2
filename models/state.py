#!/usr/bin/python3
"""State Module for HBNB project."""
import os
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel, Base):
    """Represents a State."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Get a list of all cities in State object."""
            city_l = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l

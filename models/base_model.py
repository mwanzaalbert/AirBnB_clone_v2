#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models.

    Attributes_:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Instantiate a new model.

        Parameters_:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Update updated_at with current time when instance is changed."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert BaseModel instance into dict format."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = str(type(self).__name__)

        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        dict_copy.pop("_sa_instance_state", None)

        return dict_copy

    def delete(self):
        """Delete instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Representation of the instance as a String."""
        dict_copy = self.__dict__.copy()
        dict_copy.pop("_sa_instance_state", None)

        return "[{}] ({}) {}".format(type(self).__name__, self.id, dict_copy)

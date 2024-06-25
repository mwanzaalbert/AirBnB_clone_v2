#!/usr/bin/python3
"""Module defines a base class for all models in our hbnb clone."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

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
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

            if not hasattr(kwargs, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(kwargs, 'created_at'):
                setattr(self, 'created_at', datetime.now())
            if not hasattr(kwargs, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Update updated_at with current time when instance is changed."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__

        res = dict()

        for key, value in dict_copy.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value

        return res

    def delete(self):
        """Delete instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Representation of the instance as a String."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

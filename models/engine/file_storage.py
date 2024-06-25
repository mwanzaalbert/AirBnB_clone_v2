#!/usr/bin/python3
"""Module defines a class to manage file storage for hbnb clone."""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from importlib import import_module


class FileStorage:
    """Manages storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """Initialize instance."""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """
        Retrieve entries in the FileStorage instance .

        Args_:
            cls: if specified return a dictionary of objects of the specified
                type. Otherwise, the __objects dictionary is returned.
        """
        if cls:
            filtered_dict = dict()
            for key, value in self.__objects.copy().items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )
#         self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Save storage dictionary to file."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            temp = dict()

            for key, val in self.__objects.items():
                temp[key] = val.to_dict()

            json.dump(temp, f)

    def reload(self):
        """Load storage dictionary from file."""
        classes = self.model_classes

        try:
            temp = {}
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Remove obj from __objects."""
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call the reload method."""
        self.reload()

#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Manages storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = dict()

    def all(self, cls=None):
        """
        Retrieve entries in the FileStorage instance .

        Args_:
            cls: if specified return a dictionary of objects of the specified
                type. Otherwise, the __objects dictionary is returned.
        """
        if cls:
            cls_dict = dict()
            for key, value in self.__objects.items():
                if type(value) is cls:
                    cls_dict[key] = value
            return cls_dict

        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Save storage dictionary to file."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            temp = dict()
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Load storage dictionary from file."""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
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
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call the reload method."""
        self.reload()

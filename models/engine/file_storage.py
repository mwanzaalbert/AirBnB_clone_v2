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

    # model_classes =

    # def __init__(self):
    #     """Initialize instance."""

    def all(self, cls=None):
        """
        Retrieve entries in the FileStorage instance .

        Args_:
            cls: if specified return a dictionary of objects of the specified
                type. Otherwise, the __objects dictionary is returned.
        """
        if cls:
            return {key: value for key,
                    value in self.__objects.items() if type(value) is cls}
        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        # Generate the key for the object
        key = f"{obj.__class__.__name__}.{obj.id}"

        # # Update __objects dictionary with the object
        self.__objects[key] = obj

    def save(self):
        """Save storage dictionary to file."""
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            temp = {key: value.to_dict() for key,
                    value in self.__objects.items()}

            json.dump(temp, file)

    def reload(self):
        """Load storage dictionary from file."""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        if os.path.isfile(self.__file_path):
            # try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    self.all()[key] = classes[value['__class__']](**value)
        # except FileNotFoundError:
            # pass

    def delete(self, obj=None):
        """Remove obj from __objects."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                # self.__objects.pop(key, None)
                del self.__objects[key]
                self.save()

    def close(self):
        """Call the reload method."""
        self.reload()

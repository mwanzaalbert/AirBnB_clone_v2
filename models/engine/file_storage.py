#!/usr/bin/python3
"""Module defines a class to manage file storage for hbnb clone."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Manage storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of models currently in storage.

        If a class is specified, return a dictionary of objects of that class.
        """
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            return {key: value for key, value in FileStorage.__objects.items()
                    if isinstance(value, cls)}
        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save storage dictionary to file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: val.to_dict() for key,
                    val in self.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Load storage dictionary from file."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    if cls_name in classes:
                        self.__objects[key] = classes[cls_name](**val)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Remove object from storage dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Call the reload for deserializing the JSON file to objects."""
        self.reload()

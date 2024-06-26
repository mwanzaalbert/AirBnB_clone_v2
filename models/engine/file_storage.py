#!/usr/bin/python3
"""Module defines a class to manage file storage for hbnb clone."""
import json
from importlib import import_module


class FileStorage:
    """Manage storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    classes = {
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
            return {key: value for key,
                    value in self.__objects.items() if isinstance(value, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        # Generate the key for the object
        key = f"{obj.__class__.__name__}.{obj.id}"

        # # Update __objects dictionary with the object
        self.all().update({key: obj})

    def save(self):
        """Save storage dictionary to file."""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            temp = {key: value.to_dict() for key,
                    value in FileStorage.__objects.copy().items()}

            json.dump(temp, file)

    def reload(self):
        """Load storage dictionary from file."""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    self.all()[key] = self.classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Remove obj from __objects."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                # self.__objects.pop(key, None)
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """Call the reload method."""
        self.reload()

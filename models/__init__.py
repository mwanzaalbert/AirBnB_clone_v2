#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage.

depending on the env variable value.

The database storage engine instantiates (DBStorage) when the env variable
"HBNB_TYPE_STORAGE" is encountered
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

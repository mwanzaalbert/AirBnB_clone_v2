#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage.

depending on the env variable value.

The database storage engine instantiates (DBStorage) when the env variable
"HBNB_TYPE_STORAGE" is encountered
"""
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

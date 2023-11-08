#!/usr/bin/python3
""" The FileStorage class to serialize instances to a JSON. """


import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage Class
    This handles the serialization and deserialization of instances to
    and from a JSON file.

    Attributes:
        A dictionary that stores instances as a key_value

    Methods:
        Retrieves, adds, serialiazes, and deserializes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all stored instances."""
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new instanc to the __objects dictionary. """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file. """
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects if it exists.
        If the file doesn't exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj_class, obj_id = key.split(".")
                    cls = BaseModel if obj_class == "BaseModel" else None
                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

#!/usr/bin/python3
""" The FileStorage class to serialize instances to a JSON. """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        key = "{}.{}".format(object.__class__.__name__, object.id)
        FileStorage.__objects[key] = object

    def save(self):
        """ Serialize __objects to the JSON file. """
        serialized_objects = {}
        for key, object in FileStorage.__objects.items():
            serialized_objects[key] = object.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects if it exists.
        If the file doesn't exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, object_id = key.split(".")
                    cls = None

                    if class_name == "BaseModel":
                        cls = BaseModel
                    elif class_name == "User":
                        cls = User
                    elif class_name == "State":
                        cls = State
                    elif class_name == "City":
                        cls = City
                    elif class_name == "Amenity":
                        cls = Place
                    elif class_name == "Place":
                        cls = Place
                    elif class_name == "Review":
                        cls = Review

                    if cls:
                        object = cls(**value)
                        FileStorage.__objects[key] = object
        except FileNotFoundError:
            pass

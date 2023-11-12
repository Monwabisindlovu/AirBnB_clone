#!/usr/bin/python3
""" The FileStorage class is responsible for serializing
and deserializing instances of various model classes into a JSON file. """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Filestorage class definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
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
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
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
                        cls = Amenity
                    elif class_name == "Place":
                        cls = Place
                    elif class_name == "Review":
                        cls = Review

                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of classes from the current storage"""
        return FileStorage.__objects

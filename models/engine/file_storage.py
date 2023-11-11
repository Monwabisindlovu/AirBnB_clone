#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
<<<<<<< HEAD
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
=======
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
<<<<<<< HEAD
>>>>>>> 37e47d09796754a37998f68cbc3473bcfdc7d617
=======
>>>>>>> 37e47d09796754a37998f68cbc3473bcfdc7d617

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
<<<<<<< HEAD
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: eval(v['__class__'])(**v) for k, v in json.load(f).items()}
=======
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
                        cls = Place
                    elif class_name == "Place":
                        cls = Place
                    elif class_name == "Review":
                        cls = Review

                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 37e47d09796754a37998f68cbc3473bcfdc7d617
=======
>>>>>>> 37e47d09796754a37998f68cbc3473bcfdc7d617
>>>>>>> cf3daf768f0eb46967eab9baa88f40c44fb6b61b
        except FileNotFoundError:
            pass

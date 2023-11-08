#!/usr/bin/python3
""" BaseModel module this module defines the BaseModel class """

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Initialize a new BaseModel instance with a unique ID
    and timestamps.
    """
    def __init__(self, *args, **kwargs):
        """ Initialize a new Basemodel """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ Return a tring representation of the BaseModel instance """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """ Update the updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Convert the BaseModel instance to a dict for serilization. """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict

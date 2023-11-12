#!/usr/bin/python3
""" The User class is a subclass of the BaseModel class
and represents a user. """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class of BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

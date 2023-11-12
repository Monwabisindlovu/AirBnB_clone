#!/usr/bin/python3
""" The Review class is a subclass of the BaseModel class
and represents a review associated with a certain entity,
such as a place or a service. """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class of BaseModel """
    place_id = ""
    user_id = ""
    text = ""

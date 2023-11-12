#!/usr/bin/python3
""" The Amenity class.The Amenity class represents a specific amenity that
can be associated with a certain location, property, or entity."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class """
    name = ""

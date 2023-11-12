#!/usr/bin/python3
""" This is City class.The City class is a subclass of the
BaseModel class and represents a city """

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

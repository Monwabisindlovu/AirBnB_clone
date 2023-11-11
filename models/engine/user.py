#!/usr/bin/python3
""" This is user file """
from models.base_model import BaseModel


class User(BaseModel):
    """User class - Represents a user in the Airbnb application"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

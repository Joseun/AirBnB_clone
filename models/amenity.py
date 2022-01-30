#!/usr/bin/python3
"""Defining the class Amenity """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid

class Amenity(BaseModel):
    """Defines the class Amenity """

    name = ''

    def __init__(self):
        """Intialize a new Amenity.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): private attribute
            y (int): private attribute
        """
        super().__init__(id, created_at, updated_at)
        self.id = id
        self.created_at = created_at
        self.updated_At = updated_at

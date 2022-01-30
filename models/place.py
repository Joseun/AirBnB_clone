#!/usr/bin/python3
"""Defining the class Place """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid

class Place(BaseModel):
    """Defines the class Place """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night =  0
    latitude = 0.0
    longitude = 0.0
    amenity_ids= []

    def __init__(self):
        """Intialize a new State.
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

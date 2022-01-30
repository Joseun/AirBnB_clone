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
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

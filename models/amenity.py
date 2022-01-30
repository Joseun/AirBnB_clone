#!/usr/bin/python3
"""Defining the class Amenity """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid

class Amenity(BaseModel):
    """Defines the class Amenity """

    name = ''

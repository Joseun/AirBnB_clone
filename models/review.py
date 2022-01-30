#!/usr/bin/python3
"""Defining the class Review """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid

class Review(BaseModel):
    """Defines the class Review """

    place_id = ''
    user_id = ''
    text = ''

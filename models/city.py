#!/usr/bin/python3
"""Defining the class City """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid

class City(BaseModel):
    """Defines the class User """

    state_id = ''
    name = ''

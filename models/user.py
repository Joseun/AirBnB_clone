#!/usr/bin/python3
"""Defining the class User """
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid


class User(BaseModel):
    """Defines the class User """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

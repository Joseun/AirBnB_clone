#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
import uuid


class FileStorage:
    """This is an empty class that defines a FileStorage"""

    __file_path = None
    __objects = None

    def all(self):
        """ Method JSON string
        Args:
            - list_dictionaries: list of dicts
            Returns: JSON representation of the list
        """

    def new(self, obj):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """

     def save(self):
         """ Method JSON string
        Args:
            - list_dictionaries: list of dicts
            Returns: JSON representation of the list
        """

    def reload(self):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """

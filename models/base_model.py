#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
import uuid


class BaseModel:
    """This is an empty class that defines a BaseModel"""

    def __init__(self, id=None, created_at=0, updated_at=0):
        """This is the initialiazation function for Base
        Args:
            id(:obj:'int'): public instance
        """

        self.id = id
        if self.id is None:
            id = str(uuid.uuid4())
        self.id = id

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns to standard output the details of the base model"""

        return str("[{}] ({}) {}".format(__class__.__name__, self.id,
                                         self.__dict__,))

    def save(self):
        """Updates the public instance attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing contents of __dict__ instance"""

        my_dict = {
            '__class__': __class__.__name__,
            'id': self.id,
            'created_at': datetime.isoformat(self.created_at),
            'updated_at': datetime.isoformat(self.updated_at)
        }
        return my_dict

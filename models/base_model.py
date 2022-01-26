#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
from models.engine.file_storage import storage
import uuid


class BaseModel:
    """This is an empty class that defines a BaseModel"""

    def __init__(self, id=None, created_at=0, updated_at=0, *args, **kwargs):
        """This is the initialiazation function for Base
        Args:
            id(:obj:'int'): public instance
        """

        self.id = id
        if self.id is None:
            self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            if key == "id":
                self.id = value
            if key == "created_at":
                self.created_at = datetime.strptime(value,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if key == "updated_at":
                self.updated_at = datetime.strptime(value,
                                                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Returns to standard output the details of the base model"""

        return str("[{}] ({}) {}".format(__class__.__name__, self.id,
                                         self.__dict__,))

    def save(self):
        """Updates the public instance attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing contents of __dict__ instance"""

        my_dict = {}
        for k, v in self.__dict__.items():
                my_dict[k] = v
        my_dict['__class__']= __class__.__name__
        my_dict['created_at']: datetime.isoformat(self.created_at)
        my_dict['updated_at']: datetime.isoformat(self.updated_at)
        return my_dict

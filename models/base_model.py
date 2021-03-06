#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
# import storage
import uuid


class BaseModel:
    """This is an empty class that defines a BaseModel"""

    def __init__(self, *args, **kwargs):
        """This is the initialiazation function for Base
        Args:
            id(:obj:'int'): public instance
        """

        from models import storage
        tf = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) != 0:
            kwargs.pop('__class__')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], tf)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], tf)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """Returns a dictionary containing contents of __dict__ instance"""

        from models import storage
        my_dict = {}
        for k, v in self.__dict__.items():
            my_dict[k] = v
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = (my_dict['created_at']).isoformat()
        my_dict['updated_at'] = (my_dict['updated_at']).isoformat()
        # print("======={}".format(my_dict))
        # print("##########{}".format(self.__dict__))
        return my_dict

    def __str__(self):
        """Returns to standard output the details of the base model"""

        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     str(self.__dict__)))

    def save(self):
        """Updates the public instance attribute """

        from models import storage
        self.updated_at = datetime.now()
        # storage.new(self)
        storage.save()

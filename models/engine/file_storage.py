#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
import uuid
import models


class FileStorage:
    """This is an empty class that defines a FileStorage"""

    __file_path = "AirBNBfile.json"
    __objects = {}

    def to_dict(self):
        """Returns a dictionary containing contents of __dict__ instance"""

        my_dict = {}
        for k, v in self.__dict__.items():
            my_dict[k] = v
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        #print("======={}".format(my_dict))
        #print("##########{}".format(self.__dict__))
        return my_dict

    def all(self):
        """ Method JSON string
        Args:
            - list_dictionaries: list of dicts
            Returns: JSON representation of the list
        """
        print("checking the all method {}".format(FileStorage.__objects))
        return FileStorage.__objects

    def new(self, obj):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """

        class_id = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[class_id] = obj


    @classmethod
    def save(self):
        """ Method JSON string
        Args:
            - list_dictionaries: list of dicts
            Returns: JSON representation of the list
        """
        list_dicts = []
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
            filecontent = f.read(1)
        if filecontent:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                list_dicts = json.load(f)
        else:
            list_dicts = []
        print("listdicts is this{}".format(list_dicts))
        dict_obj = {}
        print("%%%%%&&&&&#### self.objects {}".format(self.__objects))
        for k, v in self.__objects.items():
            #print(dir(v))
            dict_obj[k] = v.to_dict()
            list_dicts.append(dict_obj)
        print("======")
        print(dict_obj)
        print("#########")
        print(list_dicts)
        print("=======")
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(list_dicts, f)

    def reload(self):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """
        instance_dict = {}
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
            filecontent = f.read(1)
            print("filecontent is this {}".format(filecontent))
            if filecontent == '[':
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    print("filecontent is this {}".format(filecontent))
                    list_dicts = json.load(f)
                    print("list_dicts is this{}".format(list_dicts))
                    for dicts in list_dicts:
                        for key, inst_dict in dicts.items():
                            class_name = key.split('.')[0]
                            if class_name == 'BaseModel':
                                for k, v in inst_dict.items():
                                    instance_dict[k] = v
                    FileStorage.__objects[class_name] = instance_dict
                    print("reload output {}".format(FileStorage.__objects))
                    return FileStorage.__objects
            else:
                return instance_dict
        #except Exception as e:
            #print(e)
       # return instance_dict

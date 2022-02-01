#!/usr/bin/python3
"""Defining the class BaseModel"""
from datetime import datetime
import json
from json import dump, load, dumps
import uuid
from os import path, stat
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

name_class = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review
}

class FileStorage:
    """This is an empty class that defines a FileStorage"""

    __file_path = "AirBNBfile.json"
    __objects = {}

    def all(self):
        """ Method JSON string
        Args:
            - list_dictionaries: list of dicts
            Returns: JSON representation of the list
        """

        #self.reload()
        #print("checking the all method {}".format(FileStorage.__objects))
        return (FileStorage.__objects)

    def new(self, obj):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """
        # print('this is aobj in new oooo  {}'.format(obj))
        class_name = obj.__class__.__name__
        id = obj.id
        class_id = class_name + "." + id
        # class_id = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[class_id] = obj

    def write_json(new_data):
        """ Initaliases the FileStorage"""

        if not stat(FileStorage.__file_path).st_size == 0:
            with open(FileStorage.__file_path, 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
        else:
            file_data = {}
        # Join new_data with file_data inside emp_details
        x = file_data
        x.update(new_data)
        # Sets file's current position at offset.
        with open(FileStorage.__file_path, 'r+') as file:
            # file.seek(0)
            # convert back to json.
            json.dump(x, file, indent=4)

    def update(self, class_id, update_data):
        """ #Method JSON string
        #Args:
         #   - list_dictionaries: list of dicts
          #  Returns: JSON representation of the list
        """
        dict_obj = {}
        for k, v in FileStorage.__objects.items():
            dict_obj[k] = v.to_dict()
        if not stat(FileStorage.__file_path).st_size == 0:
            with open(FileStorage.__file_path, 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
        else:
            file_data = {}
        # Join new_data with file_data inside emp_details
        x = file_data
        print("data in update fucntion{}>>>>>>......".format(update_data))
        x[class_id] = update_data
        print("new updated json {}--------------------;;;;;".format(x))
        # Sets file's current position at offset.
        with open(FileStorage.__file_path, 'r+') as file:
            # file.seek(0)
            # convert back to json.
            json.dump(x, file, indent=4)

    def save(self):
        """ #Method JSON string
        #Args:
         #   - list_dictionaries: list of dicts
          #  Returns: JSON representation of the list
        """

       # with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
       # filecontent = f.read()
       # if filecontent:
       # with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
       # list_dicts = json.load(f)
       # else:
       # list_dicts = []
       # print("listdicts is this{}".format(list_dicts))
        dict_obj = {}
        # print("%%%%%&&&&&#### self.objects {}".format(self.__objects))
        for k, v in FileStorage.__objects.items():
            dict_obj[k] = v.to_dict()
        # print("listdicts  *****is this{}".format(dict_obj))
        # if k == '__class__':
        #   nam = dict_obj[k]
        # if k == 'id':
        # cls_id = dict_obj[k]
        # cls_id = ("{}".format(k))
        FileStorage.write_json(dict_obj)
        # print(dir(v))
        # dict_obj[k] = v.to_dict()
        # list_dicts.append(dict_obj)
        # print("======")
        # print(dict_obj)
        # print("#########")
        # print(list_dicts)
        # print("=======")"""
        # with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
        #    json.dump(dict_obj, f)

    def reload(self):
        """Returns the list of the JSON string representation
        Args:
            - json_string: string to convert to list
        """
        x = {}
        try:
            if path.isfile(FileStorage.__file_path):
                if not stat(FileStorage.__file_path).st_size == 0:
                    with open(FileStorage.__file_path, 'r') as f:
                        # filecontent = f.read()
                        # print("filecontent is this {}".format(filecontent))
                        # if filecontent:
                        #   with open(FileStorage.__file_path, 'r') as f:
                        #   print("filecontent is this {}".format(filecontent))
                        obj_dicts = json.load(f)
                        #      print("list_dicts is this{}".format(list_dicts))
                    for key, value in obj_dicts.items():
                        # for key, inst_dict in dicts.items():
                        # print(key)
                        class_name = value['__class__']
                        # print(class_name)
                        for k, v in name_class.items():
                            # print('name_class line =={}'.format(name_class))
                            if class_name == k:
                                # print("it is true so it moves")
                                x[key] = (name_class[k])(**value)
                                # print(x)
                            FileStorage.__objects = x
                            # print("reload output {}".format(FileStorage.__objects))
                            # for o in obj_dicts.values():
                            #    cls_name = o["__class__"]
                            #    del o["__class__"]
                            #   self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
        #              for k, v in inst_dict.items():
        #                 instance_dict[k] = v
        #  FileStorage.__objects = list_dicts
        # print("reload output {}".format(FileStorage.__objects))
        # return FileStorage.__objects
        # else:
        #   return instance_dict
        # except Exception as e:
        # print(e)
        # return instance_dict

#!/usr/bin/python3
"""Defining the command interpreter"""
import cmd
import json
import re
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



all_objs = storage.all()
class HBNBCommand(cmd.Cmd):
    """ AirBNB command intepreter  """

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
        'City': City, 'Amenity': Amenity, 'Review': Review
    }

    prompt = '(hbnb) '

    def emptyline(self):
        """ This function ignores an empty line input\n """
        pass

    def do_create(self, line):
        """ Create a new instance of BaseModel\n """

        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for k, v in HBNBCommand.classes.items():
                if k == line:
                    obj = v()
                    storage.new(obj)
                    storage.save()
                    print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance\n """

        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] not in HBNBCommand.classes:
                print("** class name missing **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                x = ("{}.{}".format(line[0], line[1]))
                if x in all_objs:
                    print(all_objs[x])
                    return
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance of BaseModel\n """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                for k, v in self.all_objs.items():
                    x = ("{}.{}".format(line[0], line[1]))
                    if k == x:
                        del self.all_objs[k]
                        storage.save()
                        return
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ Prints string representation of all instances of BaseModel\n """

        if not line:
            for k, v in all_objs.items():
                print(str(storage.all()[k]))
        else:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in all_objs.items():
                    x = k.split('.')
                    if x[0] == line:
                        print(str(storage.all()[k]))

    def do_update(self, line):
        """ Updates an instance of BaseModel\n """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in HBNBCommand.classes:
                if len(line) > 1:
                    x = ("{}.{}".format(line[0], line[1]))
                    if x in all_objs:
                        if len(line) > 2:
                            if len(line) > 3:
                                y = all_objs[x]
                                #y = y.to_dict()
                                if line[2] in dir(y):
                                    valtype = type(getattr(y, line[2]))
                                    y.__dict__[line[2]] = valtype(line[3])
                                    #storage.update(x, y)
                                    #print(y)
                                    #HBNBCommand.classes[line[0]](**y)
                                    #HBNBCommand.classes[line[0]].save(self)
                                else:
                                    y.__dict__[line[2]] = line[3]
                                storage.new(y)
                                storage.save()
                                return
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def default(self, arg: str) -> None:
        pattern = re.compile(r'(\w+)\.(\w+)\(([\S ]*)\)')
        res = pattern.findall(arg)
        if len(res) < 1 or len(res[0]) < 3:
            super().default(arg)
            return
        class_name = res[0][0]
        command = res[0][1]
        args = res[0][2]
        if command == "all":
            self.onecmd(f"{command} {class_name}")
            return
        elif command == "count":
            count = self.do_all(f"{class_name}", count=True)
            print(count)
            return
        else:
            if "{" in args:
                self.dict_update(class_name, args)
                return
            self.onecmd(f"{command} {class_name} {args}")
            return
        super().default(arg)

    def dict_update(self, class_name: str, arg: str) -> None:
        pattern = re.compile(r'([\w\-]+),\s*(\{.*\})')
        res = pattern.findall(arg)
        if len(res) < 1:
            self.onecmd(f"update {class_name} {arg}")
            return
        id = res[0][0]
        obj_dict = res[0][1]
        obj_dict = obj_dict.strip("{}").split(",")
        for attr_str in obj_dict:
            attr = attr_str.split(":")
            name = attr[0].strip(' "')
            value = ""
            if len(attr) > 1:
                value = attr[1].strip()
                self.onecmd(f"update {class_name} {id} {name} {value}")

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ exit the program"""
        return SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()

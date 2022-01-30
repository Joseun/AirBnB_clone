#!/usr/bin/python3
"""Defining the command interpreter"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ AirBNB command intepreter  """

    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
               'City': City, 'Amenity': Amenity, 'Review': Review}
    prompt = '(hbnb)'

    def cmdloop(self, intro=None):
        return cmd.Cmd.cmdloop(self, intro)

    def parseline(self, line):
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def onecmd(self, s):
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        """ This function ignores an empty line input """
        pass

    def default(self, line):
        return cmd.Cmd.default(self)

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)

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
                    obj.save()
                    print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance\n """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] not in HBNBCommand.classes:
                print("** class name missing **")
            elif not line[1]:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if k == line[0].line[1]:
                        print(storage.all()[k])
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
            elif not line[1]:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if k == line[0].line[1]:
                        del storage.all()[k]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """ Prints string representation of all instances of BaseModel\n """
        if not line:
            for k, v in storage.all().items():
                    print(str(storage.all()[k]))
        else:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    k = k.split()
                    if k[0] == line:
                        print(str(storage.all()[k]))

    def do_update(self, line):
        """ Updates an instance of BaseModel\n """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif not line[1]:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if k == line[0].line[1]:
                        obj = storage.all()[k]
                    else:
                        print("** no instance found **")
                if not line[2]:
                    print("** attribute name missing **")
                else:
                    for k, v in obj.__dict__.items():
                        if k == line[2]:
                            obj.k = line[3]
                            obj.save()
                        else:
                            print("** value missing **")

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ exit the program"""

        return SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()

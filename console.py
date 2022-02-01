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

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
        'City': City, 'Amenity': Amenity, 'Review': Review
    }

    all_objs = storage.all()

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
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                for k, v in self.all_objs.items():
                    x = ("{}.{}".format(line[0], line[1]))
                    if k == x:
                        print(all_objs[k])
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

        storage.reload()
        if not line:
            for k, v in self.all_objs.items():
                print(str(storage.all()[k]))
        else:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in self.all_objs.items():
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
                    if x in self.all_objs:
                        if len(line) > 2:
                            if len(line) > 3:
                                y = self.all_objs[x]
                                y = y.to_dict()
                                if line[2] in y:
                                    valtype = type(y[line[2]])
                                    y[line[2]] = valtype(line[3])
                                    storage.update(x, y)
                                    # HBNBCommand.classes[line[0]].save(self)
                                    storage.reload()
                                    storage.save()
                                    return
                                else:
                                    print("** attribute doesn't exist **")
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

    '''    def onecmd(self, line):
        """Interpret the argument as though it had been typed in response
        to the prompt.
        Checks whether this line is typed at the normal prompt or in
        a breakpoint command list definition.
        """
        try:
            classname, command = line.split('.')
            if classname not in HBNBCommand.classes:
                return cmd.Cmd.onecmd(self, line)
            else:
                if command == 'all()':
                    self.do_all(classname)
                    return
                elif command == 'count()':
                    counter = 0
                    #all_objs = models.storage.all()
                    for k in all_objs.keys():
                        key = k.split('.')
                        if key[0] == classname:
                            counter += 1
                            print(counter)
                            return
                        else:
                            raw = command[command.find('(')+1:command.find(')')]
                            raw = raw.split(', ')
                            id = raw[0][1:-1]
                            c = command[0: command.find('(')]
                            cm = "{} {} {} {}".format(c, classname, id.replace('"', ''),
                                                      " ".join(raw[1:]))
                            return cmd.Cmd.onecmd(self, cm)
        except:
            return cmd.Cmd.onecmd(self, line)
    '''
    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ exit the program"""
        return SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()

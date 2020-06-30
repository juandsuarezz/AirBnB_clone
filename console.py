#!/usr/bin/python3
"""The console"""

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from ast import literal_eval
import functools
from shlex import split

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    """
    intro = "---Welcome to hbnb! Type (?) or (help) to list commands.---"
    prompt = "(hbnb)"

    #################
    # do command#
    #################

    def do_quit(self, inp):
        """command to exit the program"""
        return True

    def do_EOF(self, inp):
        """command to exit the console"""
        print("")
        return True

    def emptyline(self):
        """when line is empty do nothing"""
        return False

    def do_create(self, inp):
        """creates a new class instance"""
        arguments = inp.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in classes:
            object = classes[arguments[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(object.id)
        object.save()

    def do_show(self, inp):
        """shows string rep of an instance
        class name and id
        """
        arguments = inp.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] in classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    print(models.storage.all()[keys])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, inp):
        """deletes an instance based on class/id"""
        arguments = inp.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] in classes:
            if len(arguments) > 1:
                keys = arguments[0] + "." + arguments[1]
                if keys in models.storage.all():
                    models.storage.all().pop(keys)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, inp):
        """prints all instances if they exist"""
        arguments = inp.split()
        instance_list = []
        if len(arguments) == 0:
            for v in models.storage.all().values():
                instance_list.append(str(v))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        elif arguments[0] in classes:
            for keys in models.storage.all():
                if arguments[0] in keys:
                    instance_list.append(str(models.storage.all()[keys]))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """
        commands = line.split()
        objs = storage.all()
        if not commands:
            print("** class name missing **")
            return None
        if not commands[0] in self.classes:
            print("** class doesn't exist **")
            return None
        if len(commands) < 4:
            if len(commands) < 2:
                print("** instance id missing **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            return None
        key = "{}.{}".format(commands[0], commands[1])
        if key not in objs:
            print("** no instance found **")
            return None
        obj = objs[key]

        try:
            obj.__dict__[commands[2]] = eval(commands[3])
            obj.save()
        except Exception:
            obj.__dict__[commands[2]] = commands[3]

     #################
    # Help Functions#
    #################

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def help_create(self):
        print("Usage: create <valid class name>")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

    ##########
    #call all function#
    #########

if __name__ == '__main__':
        HBNBCommand().cmdloop()

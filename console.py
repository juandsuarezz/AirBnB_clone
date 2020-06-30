#!/usr/bin/python3
"""The console"""

import cmd
import shlex
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
from models.engine import *


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
        models.storage.reload()
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
        models.storage.reload()
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

    def do_update(self, inp):
        """ update an instance based on its UUID """
        models.storage.reload()
        if len(inp) == 0:
            print("** class name missing **")
            return
        else:
            ac = shlex.split(inp)
            if ac[0] not in classes:
                print("** class doesn't exist **")
                return
            if ac[0] in classes and len(ac) < 2:
                print("** instance id missing **")
                return
            tmp = ac[0] + '.' + ac[1]
            if tmp in models.storage.all():
                to_update = models.storage.all()[tmp].__dict__
                if len(ac) < 3:
                    print("** attribute name missing **")
                elif len(ac) < 4:
                    print("** value missing **")
                else:
                    key = ac[2]
                    try:
                        attr = type(to_update[key])
                        value = attr(ac[3])
                    except KeyError:
                        value = ac[3]
                    to_update[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")
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

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(id, attribute name, attribute value) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(id, attribute name, attribute value) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
            """Wrapper function for <class name>.action()"""
            if args[:6] == '.all()':
                self.do_all(cls_name)
            elif args[:6] == '.show(':
                self.do_show(cls_name + ' ' + args[7:-2])
            elif args[:9] == '.destroy(':
                self.do_destroy(cls_name + ' ' + args[10:-2])
            elif args[:8] == '.update(':
                if '{' in args and '}' in args:
                    new_arg = args[8:-1].split('{')
                    new_arg[1] = '{' + new_arg[1]
                else:
                    new_arg = args[8:-1].split(',')
                if len(new_arg) == 3:
                    new_arg = " ".join(new_arg)
                    new_arg = new_arg.replace("\"", "")
                    new_arg = new_arg.replace("  ", " ")
                    self.do_update(cls_name + ' ' + new_arg)
                elif len(new_arg) == 2:
                    try:
                        dict = eval(new_arg[1])
                    except:
                        return
                    for j in dict.keys():
                        self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' '
                                       + str(j) + ' ' + str(dict[j]))
                else:
                    return
            else:
                print("Not a valid command")

if __name__ == '__main__':
        HBNBCommand().cmdloop()

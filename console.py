#!/usr/bin/python3
"""
Entry point to the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    """
    intro = "Welcome to hbnb! Type ? or help to list commands"
    prompt = "(hbnb)"

    #################
    # do command#
    #################

    def do_quit(self, inp):
        return True

    def do_EOF(self, inp):
        print("")
        return True

    def emptyline(self):
        return False

    #################
    # Help Functions#
    #################
    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

if __name__ == "__main__":
    """
    Functions main
    """
    HBNBCommand().cmdloop()

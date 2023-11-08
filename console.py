#!/usr/bin/python3
"""Entry point for the Airbnb Clone command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class - Represents the command interpreter for the AirBnB Clone
    This class provided commands for interacting with the Airbnb application

    Attributes:
        prompt (str): Custom command prompt "(hbnb)"

    Methods:
        do_quit(self, arg) Exit the program
        do_EOF(self, arg): Exit the program.
        do_help(self, arg): Display help information.
        emptyline(self): Handle an empty line input.

    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit the program using EOF """
        return True

    def do_help(self, arg):
        """ Display help information """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """ Handle an empty line input """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

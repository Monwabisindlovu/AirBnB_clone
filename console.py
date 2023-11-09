#!/usr/bin/python3
"""Entry point for the Airbnb Clone command interpreter """


import cmd
import models
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """"Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.storage.classes[arg[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage._FileStorage__objects:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage._FileStorage__objects:
            print("** no instance found **")
        else:
            print(models.storage.__FileStorage__objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                models.storage.save()

    def do_all(self, arg):
        """Print all string represntation of all instances"""
        args = arg.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in models.storage._FileStorage__objects:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all()[key]
            attr_name = args[2]
            atrr_value = args[3]
            setattr(obj, attr_name, eval(attr_value))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

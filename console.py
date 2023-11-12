#!/usr/bin/python3
"""Entry point for the Airbnb Clone command interpreter """

import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    valid_classes = ["BaseModel", "User", "City", "Place", "State",
                     "Review", "Amenity"]

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
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()  # Call all with no arguments
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()  # Call all with no arguments
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                del all_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class, or all instances"""
        args = arg.split()
        all_objects = models.storage.all()
        objects_list = []
        if not arg:
            for object in all_objects.values():
                objects_list.append(str(object))
            print(objects_list)
        else:
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objects.items():
                objects_list.append(str(obj))
            print(objects_list)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            all_objects = models.storage.all(
                args[0] if len(args) > 0 else None
            )
            print(len(all_objects))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objects = models.storage.all()  # Call all with no arguments
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                instance = all_objects[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")

    def do_reset(self, arg):
        """Deletes all instances based on the class name"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            all_objects = models.storage.all()  # Call all with no arguments
            for key in list(all_objects.keys()):  # Use list to avoid RuntimeError due to change in dict size during iteration
                if key.split('.')[0] == args[0]:
                    del all_objects[key]
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


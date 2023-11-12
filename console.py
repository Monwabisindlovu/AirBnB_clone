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
            all_objects = models.storage.all()
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
            all_objects = models.storage.all()
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
            all_objects = models.storage.all()
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
            all_objects = models.storage.all()
            for key in list(all_objects.keys()):
                if key.split('.')[0] == args[0]:
                    del all_objects[key]
            models.storage.save()

    def default(self, cmd_line):
        """Executes customized models commands"""
        callback = {
                    "all": self.do_all,
                    "update": self.do_update,
                    "count": self.count,
                    "destroy": self.do_destroy,
                    "show": self.do_show
        }
        cmd_list = cmd_line.split('.')

        if len(cmd_list) >= 2:
            command = self.command(cmd_list[1])
            if command not in callback:
                cmd.Cmd.default(self, cmd_line)
                return

            if command in ("all", "count"):
                callback[command](cmd_list[0])
            elif command == "update":
                args = self.argtok(cmd_list)
                if isinstance(args, list):
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
            else:
                callback[command](self.argtok(cmd_list))
        else:
            cmd.Cmd.default(self, line)

    def command(self, arg):
        """Command complements default"""
        index = arg.find("(")
        if index == -1:
            return arg
        return arg[:index]

    def argtok(self, args):
        """ Tokenizes args, Cleans too """

        tokens = []
        tokens.append(args[0])
        try:
            my_dict = eval(
                           args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            tokens.append(((new_str.split(", "))[0]).strip('"'))
            tokens.append(my_dict)
            return tokens
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        tokens.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in tokens).strip()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

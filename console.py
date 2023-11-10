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

    def do_create(self, args):
        """"Create a new instance of BaseModel, save it, and print the id"""
        try:
            if not args:
                raise SyntaxError()
            model, *rest = args.split(" ")

            if model in self.valid_classes:
                new_instance = eval(model)()
                models.storage.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = models.storage.all()
        object = all_objects.get(key)
        if object:
            print(object)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_object = models.storage.all()
        object = all_objects.get(key)
        if object:
            del all_objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string represntation of all instances"""
        args = arg.split()
        all_objects = models.storage.all()
        objects_list = []
        if not arg:
            for object in all_objects.values():
                objects_list.append(str(object))
        else:
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            for key, object in all_objects.items():
                if key.split('.')[0] == args[0]:
                    objects_list.append(str(object))
        print(objects_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model, id = args[:2]
        print(models.storage.all().keys())
        instance = models.storage.all().get(f"{model}_{id}")
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            returni
        if len(args) < 4:
            print("** value missing **")
            return
        attr, value = args[2:4]
        setattr(instance, attr, eval(value))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

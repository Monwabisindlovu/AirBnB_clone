#!/usr/bin/python3
"""Entry point for the Airbnb Clone command interpreter """

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class - Represents the command interpreter for the AirBnB Clone
    This class provides commands for interacting with the Airbnb application

    Attributes:
        prompt (str): Custom command prompt "(hbnb)"

    Methods:
        do_quit(self, arg): Exit the program
        do_EOF(self, arg): Exit the program.
        do_help(self, arg): Display help information.
        emptyline(self): Handle an empty line input.
        precmd(self, line): Parse commands in the format <class name>.<command>()

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

    def precmd(self, line):
        """Parse commands in the format <class name>.<command>()"""
        if "." in line and "(" in line and ")" in line:
            line = line.replace(".", " ").replace("(", " ").replace(")", " ")
        return line

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
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
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
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
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                del all_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of a class, or all instances"""
        args = arg.split()
        all_objects = models.storage.all(args[0] if len(args) > 0 else None)
        objects_list = []
        if not arg:
            for obj in all_objects.values():
                objects_list.append(str(obj))
            print(objects_list)
        else:
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            class_instances = [str(obj) for key, obj in all_objects.items() if key.split('.')[0] == args[0]]
            print(class_instances)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
            print(sum(1 for obj in all_objects.values()))

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
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                instance = all_objects[key]
                if len(args) == 4:
                    setattr(instance, args[2], args[3])
                elif len(args) == 3 and args[2][0] == "{":
                    try:
                        dict_update = eval(args[2])
                        if type(dict_update) is dict:
                            for k, v in dict_update.items():
                                if k not in ["id", "created_at", "updated_at"]:
                                    setattr(instance, k, v)
                        else:
                            print("** value is not a dictionary **")
                    except:
                        print("** value is not a dictionary **")
                else:
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
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
            for key in list(all_objects.keys()):
                if key.split('.')[0] == args[0]:
                    del all_objects[key]
            models.storage.save()

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
            all_objects = models.storage.all(args[0] if len(args) > 0 else None)
            key = "{}.{}".format(args[0], args[1])
            if key in all_objects:
                del all_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

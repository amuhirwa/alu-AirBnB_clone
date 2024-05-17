#!/usr/bin/python3
"""Module to be used as a console to manage all classes."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    models = ['BaseModel', 'User', 'Amenity', 'City',
              'Place', 'Review', 'State', 'User']

    def do_create(self, line):
        """Usage: create <class>
        Creates a new instance of a class, saves it and prints the ID."""
        if len(line) == 0:
            print('** class name missing **')
            return
        arg = line.split()[0]
        try:
            obj = eval(arg + '()')
        except NameError:
            print("** class doesn't exist **")
            return
        storage.save()
        print(obj.id)

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of an instance."""
        args = line.split(' ')
        if len(args[0]) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key in storage.all():
            obj = storage.all()[obj_key]
            print(obj)
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        args = line.split(' ')
        if len(args[0]) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        list_of_objects = []
        if line == '':
            for obj in storage.all().values():
                list_of_objects.append(obj.__str__())
        else:
            args = line.split()
            if args[0] not in self.models:
                print("** class doesn't exist **")
                return
            else:
                objs = dict(filter(lambda x: args[0] in x[0],
                                   storage.all().items()))
                for obj in objs.values():
                    list_of_objects.append(obj.__str__())
        print(list_of_objects)

    def do_update(self, line):
        args = line.split(' ')
        if len(args[0]) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key in storage.all():
            instance = storage.all()[obj_key]
            if args[2] in instance.__dict__:
                attr_type = type(getattr(instance, args[2]))
                new_value = attr_type(args[3])
                instance.__dict__[args[2]] = new_value.replace('\"', '')
            else:
                instance.__dict__[args[2]] = args[3].replace('\"', '')
            instance.save()
        else:
            print('** no instance found **')
            return

    def emptyline(self):
        """Defines what happens when an empty line is ran."""
        pass

    def do_quit(self, line):
        "Exit the program"
        return True

    def do_EOF(self, line):
        "Exit the program with CTRL + D"
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

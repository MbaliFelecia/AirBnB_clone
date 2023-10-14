#!/usr/bin/python3
""" import cmd module, BaseModel and storage """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import sys

list_classes = ["BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Review",
                "Place"]


class HBNBCommand(cmd.Cmd):
    """ Command processor"""

    prompt = "(hbnb)"

    def do_create(self, arg):
        """Creates a new instance of BaseModel and 
        print id """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            obj = eval(args[0] + "()")
            id = getattr(obj, 'id')
            storage.save()
            print(id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg=""):
        """ Prints the string representtation of 
        an instance based  on the class name and id"""
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] list_classes:
            if len(args) >= 2:
                name_id = args[0] + "." + str(args[1])
                objs = storage.all()
                if name_id in objs.keys():
                    obj = objs[name_id]
                    print(obj)
                else:
                    print("* *no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Dekets an instance based on class name and id """
        args = arg.split(" ")
        if len(arg) == 0:
            print ("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 2:
                name_id = args[0] + "." + str(args[1])
                objs = storage.all()
                if name_id in objs.keys():
                    del(objs[name_id])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self,arg):
        """ Prints all string representation of
        all instances based or not on the class name """
        objs = storage.all()
        args = arg.split(" ")
        list_all = []
        if len(arg) == 0:
            for obj in objs.values():
                list_all.append(str(obj))
            print(list_all)
        elif args[0] in list_classes:
            for name_id in objs.keys():
                if name_id.split(".")[0] == args[0]:
                    list_all.append(str(objs[name_id]))
            print(list_all)
        else:
            print("** class doesn't exist **")

    def do_update(self,arg):
        """  Updates an instance based on the class name
        and id by adding or updating attribute"""
        objs = storage.all()
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) < 2:
                print("** instance id missing **")
            elif args[1] in [name_id.split(".")[1] for name_id in objs.keys()]:
                name_id = args[0] + "." + args[1]
                obj = objs [name_id]
                if len(args ) < 3:
                    print("** attribute name missing **")
                else:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                        try:
                            setattr(obj, args[2], eval(args[3].strip('"')))
                        except:
                            setattr(obj, args[2], args[3].strip('"')))
                        storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
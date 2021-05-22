#!/usr/bin/python3
"""cmdline trying to get a command line prompt up and running"""

import cmd, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class HBNBCommand(cmd.Cmd):
    """MyPrompt is a cmd class meant to get command line up and running"""
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def do_create(self, arg):
        """ Create a new instance of BaseModel, saved to JSON, print id """
        if not arg:
            print("** class name missing **")
            return
        if arg not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        newInstance = FileStorage.class_inits[arg]()
        print(newInstance.id)
        FileStorage.save(newInstance)

    def do_show(self, args):
        """ Prints the string rep of an instance based on the class name """
        cmds = args.split()
        cls_name = cmds[0]
        cls_id = cmds[1]
        if not cls_name:
            print("** class name missing **")
            return
        if not cls_id:
            print("** instance id missing **")
            return
        if cls_name not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        if "{}.{}".format(cls_name, cls_id) not in models.storage.all().keys():
            print("** no instance found **")
            return
        print(str(models.storage.all()["{}.{}".format(cls_name, cls_id)]))

    def do_destroy(self, args):
        """ Delete an instance based on class name and id """
        cmds = args.split()
        cls_name = cmds[0]
        cls_id = cmds[1]
        if not cls_name:
            print("** class name missing **")
            return
        if not cls_id:
            print("** instance id missing **")
            return
        if cls_name not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        if "{}.{}".format(cls_name, cls_id) not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()["{}.{}".format(cls_name, cls_id)]
        models.storage.save()

    def do_all(self, arg):
        """ Print all string reps of all instances based on class input """
        listOfInstances = []
        if not arg:
            for key in models.storage.all().keys():
                listOfInstances.append(str(models.storage.all()[key]))
            print(listOfInstances)
        else:
            if arg not in FileStorage.class_inits.keys():
                print("** class doesn't exist **")
            for cls_name in models.storage.all().keys():
                if arg in cls_name:
                    listOfInstances.append(str(models.storage.all()[cls_name]))
            print(listOfInstances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

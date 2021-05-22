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
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if len(cmds) == 1:
            print("** instance id missing **")
            return
        if cmds[0] not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        if "{}.{}".format(cmds[0], cmds[1]) not in models.storage.all().keys():
            print("** no instance found **")
            return
        print(str(models.storage.all()["{}.{}".format(cmds[0], cmds[1])]))

    def do_destroy(self, args):
        """ Delete an instance based on class name and id """
        cmds = args.split()
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if len(cmds) == 1:
            print("** instance id missing **")
            return
        if cmds[0] not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        if "{}.{}".format(cmds[0], cmds[1]) not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()["{}.{}".format(cmds[0], cmds[1])]
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
                return
            for cls_name in models.storage.all().keys():
                if arg in cls_name:
                    listOfInstances.append(str(models.storage.all()[cls_name]))
            print(listOfInstances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

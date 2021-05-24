#!/usr/bin/python3
"""cmdline trying to get a command line prompt up and running"""

import cmd
import sys
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
        # if <class> (id) found in storage print string rep of instance
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
        # check to make sure <class> exists
        if cmds[0] not in FileStorage.class_inits.keys():
            print("** class doesn't exist **")
            return
        # confirm <class> <id> are in storage
        if "{}.{}".format(cmds[0], cmds[1]) not in models.storage.all().keys():
            print("** no instance found **")
            return
        # if <class> exists and <class> <id> pair exist - delete it
        del models.storage.all()["{}.{}".format(cmds[0], cmds[1])]
        models.storage.save()

    def do_all(self, arg):
        """ Print all string reps of all instances based on class input """
        # create empty list to return
        listOfInstances = []
        if not arg:
            # if <class> not specified print all keys appended to new list
            for key in models.storage.all().keys():
                listOfInstances.append(str(models.storage.all()[key]))
            print(listOfInstances)
        else:
            # if arg is specified, confirm it exists
            if arg not in FileStorage.class_inits.keys():
                print("** class doesn't exist **")
                return
            # if <class> name is confirmed, print all instances of that class
            for cls_name in models.storage.all().keys():
                if arg in cls_name:
                    listOfInstances.append(str(models.storage.all()[cls_name]))
            print(listOfInstances)

    def do_update(self, args):
        """updates an instance based on the class name and id"""
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
        if len(cmds) == 2:
            print("** attribute name missing **")
            return
        if len(cmds) == 3:
            print("** value missing **")
            return
        # for instance key name in "view object" of storage
        for inst_name in models.storage.all().keys():
            # store instance as [inst_name] in variable <instance>
            instance = models.storage.all()[inst_name]
            # confirm cmd[1]//<id> is in list of key names in "view object"
            if cmds[1] in inst_name:
                # if cmd[2]<class attr> is in str repr of instance
                if cmds[2] in str(instance):
                    # ******CHRIS NEEDS TO LEARN ABOUT THIS BLOCK OF CODE***
                    val = type(instance.__dict__[cmds[2]])(cmds[3])
                    setattr(instance, cmds[2], val)
                else:
                    instance.__dict__[cmds[2]] = cmds[3]
            instance.save()

    def default(self, line):
        """ Parse line based on syntax instructions, pass to other func """
        # separate input by "." delim, match 0th str with Class dict
        if "." in line and line.split(".")[0] \
                in FileStorage.class_inits.keys():
            # 0th portion is class name
            cls = line.split(".")[0]
            # method is everything after class name
            method = line[len(cls) + 1:]
            # action is the console method to call
            action = method.split("(")[0]
            # paramters, if they exist, all follow action
            params = method[method.find("(") + 1:method.find(")")]
            if action == "all":
                self.do_all(cls)
            elif action == "show":
                self.do_show(cls + " " + params[1:-1])
            elif action == "destroy":
                self.do_destroy(cls + " " + params[1:-1])
            elif action == "update":
                info = params.split(", ")
                p_id = info[0][1:-1]
                p_attr = info[1][1:-1]
                # new val for update may or may not be wrpaped in quotes
                p_val = info[2][1:-1] if info[2][0] == "\"" else info[2]
                # re-concat into a string to pass into above methods
                self.do_update(cls + " " + p_id + " " + p_attr + " " + p_val)
            elif action == "count":
                # for each key that exists in __objects, iterate
                print(len(list(filter(
                 lambda key: key.split(".")[0] == cls, models.storage.all()))))
            else:
                super().default()
        else:
            super().default()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

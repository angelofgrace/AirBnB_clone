#!/usr/bin/python3
"""cmdline trying to get a command line prompt up and running"""

import cmd, sys

class HBNBCommand(cmd.Cmd):
    """MyPrompt is a cmd class meant to get command line up and running"""
    prompt = '(hbnb)'
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

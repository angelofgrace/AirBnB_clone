#!/usr/bin/python3
"""cmdline trying to get a command line prompt up and running"""

import cmd, sys

class HBNBCommand(cmd.Cmd):
    """MyPrompt is a cmd class meant to get command line up and running"""
    intro = 'You are inside a shell you created\n'
    prompt = 'And_I_OOP$ '
    file = None

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        print('Thank you for using bloop')
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("EOF triggered, bloop was exited")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
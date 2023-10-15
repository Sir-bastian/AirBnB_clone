#!/usr/bin/python3

""" console module """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ A clas that contains the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Exit the program by typing CTRL + D """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ When you input an empty line + ENTER, it doesn’t execute anything"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """  Prints the string representation of an instance based
        on the class name and id"""
        tokens = line.split(" ")
        if tokens is None or line is = "":
            print("** class name missing **")
         else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        if line is None or line is line == "":
            print("** class name is missing **")


if __name__ == '__main__':
        HBNBCommand().cmdloop()

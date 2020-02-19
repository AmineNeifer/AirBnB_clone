#!/usr/bin/python3

"""module that contains the console"""


import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import inspect


def ifclass(str):
    """function ifclass"""
    try:
        v = inspect.isclass(eval(str))
        return(v)
    except:
        return False


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program
        """
        return True

    def emptyline(self):
        """empty line function"""
        pass

    def do_create(self, name):
        """ Do_create creates another <name> object
        """
        if name is None or name == "":
            print("** class name missing **")
        elif name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, name):
        """ shows instances of an obj
        """
        args = name.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if (
                    ifclass(args[0]) and
                    issubclass(eval(args[0]), BaseModel) is True):
                if len(args) > 1:
                    test = False
                    for k,v in FileStorage().all().items():
                        Id = k.split('.')[1]
                        if Id == args[1]:
                            print(str(v))
                            test = True
                    if test is False:
                        print("** instance id missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, name):
        """ destroy instances of an obj
        """
        args = name.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if (ifclass(args[0]) and
                issubclass(eval(args[0]), BaseModel) is True):
                if len(args) > 1:
                    del FileStorage().all()[args[0]+ '.' + args[1]]
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, name=""):
        """ print all objs
        """
        if name == "":
            for k, v in storage.all().items():
                print (v)
        else:
            if (ifclass(name) and issubclass(eval(name), BaseModel) is True):
                for k, v in storage.all().items():
                    if name == k.split(".")[0]:
                        print (v)
            else:
                print("** class doesn't exist **")

    def do_update(self, name):
        """ update an attribute in an obj
        """
        args = name.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if (ifclass(args[0]) and
                issubclass(eval(args[0]), BaseModel) is True):
                if len(args) > 1:
                    test = False
                    for k,v in storage.all().items():
                        Id = k.split('.')[1]
                        if Id == args[1]:
                            test = True
                    if test is False:
                        print("** no instance found **")
                    elif len(args) > 2:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            key = args[0] + '.' + args[1]
                            obj = storage.all()
                            if key in obj:
                                spl = args[3].split('"')
                                if len(spl) == 1:
                                    print("** value missing **")
                                else:
                                    setattr(obj[key], args[2], args[3].split('"')[1])
                                    storage.save()
                    else:
                       print("** attribute name missing **")

                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()

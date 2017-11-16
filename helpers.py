# coding: utf-8
 
import os

# returns an environment variable as uppercase
def get_env(field):
    return os.environ[field.upper()]


# return the name of the function called as first argument of command
def get_command_name(args):
    return list(args.__dict__)[0]


# return a list of the arguments passed after command.
# e.g. $ jump --upgrade arg1 arg2 would return ['arg1', 'arg2']
def get_arguments(args, command):
    return getattr(args, command)

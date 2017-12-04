# coding: utf-8
 
import sys
import os

import jumputils.commands


# returns an environment variable as uppercase
def get_env(field):
    return os.environ[field.upper()]


# return the name of the function called as first argument of command
def get_command_name(args):
    command_name = None

    for command in list(args.__dict__):
        if getattr(args, command) is not None:
            command_name = command
            break

    return command_name


# return a list of the arguments passed after command.
# e.g. $ jump --upgrade arg1 arg2 would return ['arg1', 'arg2']
def get_arguments(args, command):
    return getattr(args, command)


# Execute the correct command according to user input
def execute(parser):
    args = parser.parse_args()
    command_name = get_command_name(args)
    
    if command_name is None:
        parser.print_help()
        sys.exit(0)

    command = getattr(jump.commands, command_name)
    arguments = get_arguments(args, command_name)
    
    function = getattr(command, 'main')
    function(arguments)
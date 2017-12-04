# coding: utf-8

from fabric.api import local, run
from fabric.colors import green, red


def jump():
    local('cd ./utils && git pull && git checkout master')
    print(green('Upgrade successful.'))


def main(args):
    target = args[0]

    try:
        function = eval(target)
        function()
    except Exception as e:
        print(red('No function named %s was found in commands/upgrade.py.') % target)
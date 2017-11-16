# coding: utf-8

from fabric.api import cd, local, env, run
from fabric.colors import green


def main(args):
    local('cd ./utils && git pull && git checkout master')
    print(green('Upgrade successful.'))